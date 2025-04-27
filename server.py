from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # מאפשר קריאות מבחוץ (מהדף שלך בקוביו)

@app.route('/')
def home():
    return "Server is running! ✅"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    # כאן אפשר לחבר ל-OpenAI בעתיד, אבל כרגע נחזיר תשובה פשוטה
    ai_response = f"You asked: {user_message}. (AI Chanan replies: Stay tuned for full intelligence!)"

    return jsonify(response=ai_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
