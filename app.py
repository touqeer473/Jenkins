# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from CI/CD Pipeline!"

if __name__ == '__main__':
    app.run(host='20.17.98.51', port=8080)