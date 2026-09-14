from flask import Flask, request
import os

app = Flask(__name__)
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")

@app.route('/', methods=['GET'])
def home():
    return "Bot ya NENO LA TUMAINI iko Live ✅", 200

@app.route("/webhook", methods=['GET', 'POST'])
def verify():
    if request.method == 'GET':
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403
    
    if request.method == 'POST':
        data = request.get_json()
        print(data) # hii itatusaidia kuona ujumbe ukiingia
        return "ok", 200

if __name__ == '__main__':
    app.run()
