from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# מפתח OpenAI החדש שהבאת
openai.api_key = "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"

# היסטוריה כדי לשמור הקשר
chat_history = [
    {"role": "system", "content": "You are a professional AI assistant created by Chanan Zevin, specializing in finance, stocks, technology, and innovation."}
]

@app.route('/')
def home():
    return "Chanan AI Chat Server - Advanced version is running with new API Key! ✅"
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    model_to_use = data.get('model', 'gpt-4o')  # ברירת מחדל gpt-4o

    chat_history.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model=model_to_use,
            messages=chat_history,
            temperature=0.5,
            max_tokens=600
        )
        ai_reply = response['choices'][0]['message']['content'].strip()

        chat_history.append({"role": "assistant", "content": ai_reply})

    except Exception as e:
        ai_reply = f"Error from OpenAI: {str(e)}"

    return jsonify(response=ai_reply)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
