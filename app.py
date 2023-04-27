import os
from dotenv import load_dotenv

from src.models import db, Post,User, LikedBy
from flask import Flask, render_template
from src.repositories.post_repository import post_repository_singleton

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
with app.app_context():
    db.create_all()


@app.get("/landing")
def landing_page():
    return render_template("pages/landing_page.html", no_layout=True)


@app.get("/")
def home_page():
    posts = Post.query.all()
    users = User.query.all()
    # Assuming user is ID = 1
    likes = LikedBy.query.filter_by(user_id= 1)
    # get the post liked by the user
    return render_template("pages/home_page.html", home_active=True, posts=posts,users=users, likes=likes)


@app.get("/tunes/new")
def new_page():
    keys = [
        {"frequency": 261.63, "type": "white"},
        {"frequency": 277.18, "type": "black"},
        {"frequency": 293.66, "type": "white"},
        {"frequency": 311.13, "type": "black"},
        {"frequency": 329.63, "type": "white"},
        {"frequency": 349.23, "type": "white"},
        {"frequency": 369.99, "type": "black"},
        {"frequency": 392.00, "type": "white"},
        {"frequency": 415.30, "type": "black"},
        {"frequency": 440.00, "type": "white"},
        {"frequency": 466.16, "type": "black"},
        {"frequency": 493.88, "type": "white"},
        {"frequency": 523.26, "type": "white"},
    ]
    return render_template("pages/new_page.html", new_active=True, keys=keys)


@app.get("/tunes")
def library_page():
    return render_template("pages/library_page.html", library_active=True)


@app.get("/account")
def account_page():
    return render_template("pages/account_page.html", account_active=True)

@app.get("/post/<int:post_id>")
def post_page(post_id):
    post_info= post_repository_singleton.get_post_info(post_id)
    return render_template("pages/post.html", account_active=True, post_info = post_info)