from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/")
def home():
    delay = random.uniform(0, 2)
    time.sleep(delay)
    return {
        "status": "still ok",
        "delay_seconds": round(delay, 2)
    }

@app.route("/health")
def health():
    return "healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
