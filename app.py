from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", home_active=True)


@app.get("/account")
def account_page():
    return render_template("account.html", account_active=True)

