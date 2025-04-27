from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# כאן תכניס את המפתח שלך
openai.api_key = "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"

@app.route('/')
def home():
    return "Server is running with OpenAI connection! ✅"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # או gpt-3.5-turbo אם תרצה
            messages=[
                {"role": "system", "content": "You are a professional AI assistant answering about stocks, finance, and technology, created by Chanan Zevin."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.5,
            max_tokens=500
        )
        ai_reply = response['choices'][0]['message']['content'].strip()

    except Exception as e:
        ai_reply = f"Error from OpenAI: {str(e)}"

    return jsonify(response=ai_reply)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
