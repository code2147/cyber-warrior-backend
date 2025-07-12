from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

RAPIDAPI_KEY = os.environ.get("c66bf656f3msh1922e7e078a5b47p151649jsn18c010a991ec")

@app.route("/check")
def check():
    account = request.args.get("account")
    if not account:
        return jsonify({"error": "No account provided"}), 400

    url = f"https://haveibeenpwned.p.rapidapi.com/breachedaccount/{account}"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "haveibeenpwned.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        return jsonify([])  # No breaches found
    elif response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "API call failed", "details": response.text}), response.status_code

if __name__ == "__main__":
    app.run()
