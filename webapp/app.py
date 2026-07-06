from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test-function")
def test_function():

    try:
        response = requests.get("http://localhost:7071/api/GetServerTime")
        return jsonify(response.json())

    except Exception as e:
        return jsonify({
            "status": "Error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)