from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log_access():
    data = request.get_json()
    email = data.get("email")
    duration = data.get("duration")
    timestamp = datetime.utcnow().isoformat()

    new_entry = {
        "email": email,
        "duration_days": duration,
        "timestamp": timestamp
    }

    with open("access_log.json", "r+") as f:
        log_data = json.load(f)
        log_data.append(new_entry)
        f.seek(0)
        json.dump(log_data, f, indent=2)

    return jsonify({"status": "logged", "entry": new_entry}), 200

if __name__ == "__main__":
    app.run(debug=True)
