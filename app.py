from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.run(host="0.0.0.0", port=10000)
@app.route("/")
def home():
    return "<h2>Welcome — Portfolio is at /portfolio</h2>"

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run(debug=True)
