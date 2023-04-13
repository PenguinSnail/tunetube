import os
from dotenv import load_dotenv

from src.models import db, Posts
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")


app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)


@app.get("/landing")
def landing_page():
    return render_template("pages/landing_page.html")


@app.get("/")
def home_page():
    post = Posts.query.all()
    return render_template("pages/home_page.html", home_active=True, post=post)


@app.get("/tunes/new")
def new_page():
    return render_template("pages/new_page.html", new_active=True)


@app.get("/tunes")
def library_page():
    return render_template("pages/library_page.html", library_active=True)


@app.get("/account")
def account_page():
    return render_template("pages/account_page.html", account_active=True)
