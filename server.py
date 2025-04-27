from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "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"

# רשימת הודעות לשמירת השיחה
chat_history = [
    {"role": "system", "content": "You are a professional AI assistant created by Chanan Zevin, specializing in finance, stocks, technology, and innovation."}
]

@app.route('/')
def home():
    return "Chanan AI Chat Server - Advanced version is running! ✅"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    model_to_use = data.get('model', 'gpt-4o')  # ברירת מחדל GPT-4o, אפשר לשלוח גם gpt-3.5-turbo

    # הוסף את הודעת המשתמש להיסטוריה
    chat_history.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model=model_to_use,
            messages=chat_history,
            temperature=0.5,
            max_tokens=600
        )
        ai_reply = response['choices'][0]['message']['content'].strip()

        # שמור את תשובת ה-AI להיסטוריה
        chat_history.append({"role": "assistant", "content": ai_reply})

    except Exception as e:
        ai_reply = f"Error from OpenAI: {str(e)}"

    return jsonify(response=ai_reply)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
