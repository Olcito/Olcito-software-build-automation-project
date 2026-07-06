from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test-function")
def test_function():
    return jsonify({
        "status": "Success",
        "message": "Hello from Azure Function!",
        "student": "Olcayto Koruk",
        "course": "Software Build Automation Tools",
        "server_time": "2026-07-06"
    })

    try:
        response = requests.get("https://sba-function-olcito-h5a3gudjcjefazc5.swedencentral-01.azurewebsites.net/api/GetServerTime")
        return jsonify(response.json())

    except Exception as e:
        return jsonify({
            "status": "Error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)