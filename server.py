from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OPENAI_API_KEY = "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"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json',
    }
    payload = {
        'model': 'gpt-4o',
        'messages': [{'role': 'user', 'content': user_message}],
        'temperature': 0.5,
        'max_tokens': 500,
    }

    try:
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        ai_reply = data['choices'][0]['message']['content'].strip()
        return jsonify({'response': ai_reply})
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)