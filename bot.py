import os
from flask import Flask, request

app = Flask(__name__)
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

@app.route('/', methods=['GET'])
def home():
    return "Bot ya NENO LA TUMAINI iko Live ✅", 200

@app.route('/webhook', methods=['GET'])
def verify():
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if token == VERIFY_TOKEN:
        return challenge, 200
    return "Verification failed", 403

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Message mpya:", data)
    return "ok", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
