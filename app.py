from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", home_active=True)


@app.get("/landing_page")
def landing_page():
    return render_template("landing_page.html")
