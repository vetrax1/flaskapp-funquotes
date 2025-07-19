from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Keep it simple.",
    "DevOps is a culture, not a role.",
    "Fail fast, recover faster.",
    "Automation beats repetition."
]

@app.route("/")
def quote():
    return random.choice(quotes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)