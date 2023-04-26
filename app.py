import os
from dotenv import load_dotenv

from src.models import db, Post, User
from flask import Flask, render_template, redirect, request, abort
from flask_bcrypt import Bcrypt

load_dotenv()

app = Flask(__name__)
bcrypt = Bcrypt(app)

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
    all_posts = Post.query.all()
    return render_template("pages/home_page.html", home_active=True, posts=all_posts)


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

@app.route("/account/register", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":  # actually making account
        name = request.form.get("name")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not password or not name or not confirm_password:
            abort(400)
            # TODO change these aborts to proper error messages

        if password != confirm_password:
            abort(400)
        
        if User.query.filter(User.username.ilike(name)).first() is not None:
            abort(400)

        # all fields filled out

        hashed_password = bcrypt.generate_password_hash(password).decode()

        user = User(username=name, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    # get request
    return render_template("pages/sign_up_page.html")

# @app.route("/login", methods=["GET", "POST"])
@app.post("/login")
def login_info():
    name = request.form.get("name")
    password = request.form.get("password")

    if not password or not name:
        return redirect("/login")

    confirm_user = User.query.filter(User.username.ilike(name)).first()

    if not confirm_user:
        return redirect("/login")
    
    if not bcrypt.check_password_hash(confirm_user.password, password):
        return redirect("/login")

    return redirect('/')  
    # rediret tot he correct page if everything checks out.

@app.get("/login")
def login_page():
    return render_template("pages/login.html")