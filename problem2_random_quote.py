from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
]

@app.route('/')
def get_quote():
    return random.choice(quotes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
