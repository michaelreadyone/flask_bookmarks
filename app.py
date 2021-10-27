from flask import Flask, jsonify


app = Flask(__name__)

@app.get("/hello")
def index():
    return jsonify({"message": "Hello world"})