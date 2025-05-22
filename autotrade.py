from flask import Flask, request, jsonify

app = Flask(__name__)
IN_POSITION = False

@app.route("/webhook", methods=["POST"])
def webhook():
    global IN_POSITION
    data = request.json
