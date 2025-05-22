from flask import Flask, request, jsonify
import os

app = Flask(__name__)
IN_POSITION = False

@app.route("/webhook", methods=["POST"])
def webhook():
    global IN_POSITION
    data = request.json
    action = data.get("action")

    print(f"[Webhook Received] action={action}, in_position={IN_POSITION}")

    if action == "buy" and not IN_POSITION:
        print("[MOCK BUY] 30% 진입 × 5배 레버리지")
        IN_POSITION = True
        return jsonify({"status": "buy executed"})

    elif action == "sell" and IN_POSITION:
        print("[MOCK SELL] 전체 청산")
        IN_POSITION = False
        return jsonify({"status": "sell executed"})

    return jsonify({"status": "ignored"})

@app.route("/")
def root():
    return "✅ BTC AutoTrade Flask 서버 작동 중 (Render 버전)"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render는 포트를 환경변수로 지정함
    app.run(host="0.0.0.0", port=port)
