from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Dockerized Flask API",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "health": "ok"
    })

@app.route("/status")
def status():
    return jsonify({
        "service": "flask-api",
        "environment": "dev",
        "status": "active"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)