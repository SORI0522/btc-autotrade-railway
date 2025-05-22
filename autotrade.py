# Render 배포용 Flask 자동매매 서버 (logging 포함)
from flask import Flask, request, jsonify
import os
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
IN_POSITION = False

@app.route("/webhook", methods=["POST"])
def webhook():
    global IN_POSITION
    data = request.json
    action = data.get("action")

    logging.info(f"[Webhook Received] action={action}, in_position={IN_POSITION}")

    if action == "buy" and not IN_POSITION:
        logging.info("[MOCK BUY] 30% 진입 × 5배 레버리지")
        IN_POSITION = True
        return jsonify({"status": "buy executed", "in_position": IN_POSITION})

    elif action == "sell" and IN_POSITION:
        logging.info("[MOCK SELL] 전체 청산")
        IN_POSITION = False
        return jsonify({"status": "sell executed", "in_position": IN_POSITION})

    return jsonify({"status": "ignored", "in_position": IN_POSITION})

@app.route("/")
def root():
    return "✅ BTC AutoTrade Flask 서버 작동 중 (Render 배포 버전)"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
