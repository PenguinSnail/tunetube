from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", home_active=True)


@app.get("/home")
def home_page():
    return render_template("home-page.html", home_active=True)
