from flask import Flask, render_template


app = Flask(__name__)


@app.get("/landing")
def landing_page():
    return render_template("pages/landing_page.html")


@app.get("/")
def home_page():
    return render_template("pages/home_page.html", home_active=True)


@app.get("/editor")
def editor_page():
    return render_template("pages/editor_page.html", editor_active=True)


@app.get("/library")
def library_page():
    return render_template("pages/library_page.html", library_active=True)


@app.get("/account")
def account_page():
    return render_template("pages/account_page.html", account_active=True)
