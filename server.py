from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Create OpenAI client using the API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initial system prompt for chat
chat_history = [
    {"role": "system", "content": "You are a professional AI assistant created by Chanan Zevin, specializing in finance, stocks, technology, and innovation."}
]

@app.route('/')
def home():
    return "Chanan AI Chat Server - Connected to OpenAI successfully! ✅"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    model_to_use = data.get('model', 'gpt-4o')

    chat_history.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model=model_to_use,
            messages=chat_history,
            temperature=0.5,
            max_tokens=600
        )
        ai_reply = response.choices[0].message.content.strip()

        chat_history.append({"role": "assistant", "content": ai_reply})

    except Exception as e:
        ai_reply = f"Error from OpenAI: {str(e)}"

    return jsonify(response=ai_reply)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
