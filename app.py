from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", home_active=True)


@app.get("/editor")
def note_creation():
    return render_template("note_creation.html")
