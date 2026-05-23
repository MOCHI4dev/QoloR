from flask import Flask, request, jsonify, send_file
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from encoder import encode

app = Flask(__name__)


@app.route("/")
def index():
    return "color-qr ugoiteruyo"


@app.route("/encode", methods=["POST"])
def encode_route():
    data = request.json.get("data", "hello")
    output_path = "output/test.png"
    encode(output_path=output_path)
    return send_file(output_path, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
