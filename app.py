from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", home_active=True)


@app.get("/library")
def library():
    return render_template("tune_library.html", home_active=True)
