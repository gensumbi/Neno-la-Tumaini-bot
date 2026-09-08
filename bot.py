import requests
import os
from flask import Flask, request

app = Flask(__name__)

PHONE_NUMBER_ID = "1281300705072739" 
ACCESS_TOKEN = "2732798583785111"

def send_whatsapp_message(to, text):
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    requests.post(url, headers=headers, json=data)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return request.args.get("hub.challenge")
    
    data = request.get_json()
    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]
        from_number = message["from"]
        msg_body = message["text"]["body"]

        reply = f"Neno la Tumaini kwako leo: \n\nMungu ni kimbilio na nguvu yako. Usife moyo, yeye yupo pamoja nawe. 🙏"
        send_whatsapp_message(from_number, reply)

    except Exception as e:
        print(e)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
