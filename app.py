import os
from dotenv import load_dotenv

from src.models import db, Post, User, FollowedBy, Comment, LikedBy
from flask import Flask, render_template, redirect, request, abort, session
from flask_bcrypt import Bcrypt
from src.repositories.post_repository import post_repository_singleton
from src.repositories.user_repository import user_repository_singleton


# Environment variables
load_dotenv()
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")


# App initialization
app = Flask(__name__)
bcrypt = Bcrypt(app)


# Database connection
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
# app.config["SQLALCHEMY_ECHO"] = True

app.secret_key = os.getenv("APP_SECRET")

# Database initialization
db.init_app(app)
with app.app_context():
    # create tables if they don't already exist
    db.create_all()


@app.get("/landing")
def landing_page():
    return render_template("pages/landing_page.html", no_layout=True)


@app.get("/")
def post_page():
    # Authentication
    if "user" not in session:
        return redirect("/landing")

    all_posts = Post.query.all()

    current_user = session["user"]["user_id"]
    user_info = user_repository_singleton.get_user_info(current_user)
    return render_template(
        "pages/home_page.html", home_active=True, posts=all_posts, user_info=user_info
    )


@app.get("/<int:user_id>")
def my_Post_page(user_id: int):
    # Authentication
    if "user" not in session:
        return redirect("/landing")

    user_posts = Post.query.filter_by(user_id)

    current_user = session["user"]["user_id"]
    user_info = user_repository_singleton.get_user_info(current_user)
    return render_template(
        "pages/home_page.html",
        home_active=True,
        user_posts=user_posts,
        user_info=user_info,
    )


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def single_post(post_id: int):
    current_user = session["user"]["user_id"]
    user_info = user_repository_singleton.get_user_info(current_user)

    if request.method == "POST":
        comment = request.form.get("create-comment", "")

        if comment == "":
            pass

        new_comment = Comment(current_user, post_id, comment)
        db.session.add(new_comment)
        db.session.commit()
        pass

    post_info = post_repository_singleton.get_post_info(post_id)
    return render_template("pages/post.html", post_info=post_info, user_info=user_info)


app.route("/like/<int:post_id>/<action>")


def like_action(post_id, action):
    current_user = session["user"]["username"]
    user_info = user_repository_singleton.get_user_info(current_user)

    if action == "like":
        newLike = LikedBy(user_info.getID, post_id)
        db.session.commit(newLike)

    if action == "unlike":
        LikedBy.query.filter_by(post_id=post_id, user_id=user_info.getID()).delete()
        db.session.commit()


@app.get("/tunes/new")
def new_page():
    # Authentication
    if "user" not in session:
        return redirect("/landing")

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
    # Authentication
    if "user" not in session:
        return redirect("/landing")

    return render_template("pages/library_page.html", library_active=True)


@app.post("/tunes")
def create_tune():
    song = request.form.get("data")
    if song:
        title = request.form.get("title")
        post = Post(title=title, song=song, user_id=session["user"]["user_id"])
        db.session.add(post)
        db.session.commit()

    return redirect("/tunes")


@app.get("/account")
def account_page():
    # Authentication
    if "user" not in session:
        return redirect("/landing")

    # get session user id
    current_user = session["user"]["user_id"]
    user_info = User.query.filter_by(id=current_user).first()

    # get list of all followers for user id
    followers_list = FollowedBy.query.filter_by(user_id=user_info.id).all()

    # get users for all followed accounts
    followed = []
    for follower in followers_list:
        followed += User.query.filter_by(id=follower.follower_id).all()

    return render_template(
        "pages/account_page.html",
        account_active=True,
        name=user_info.username,
        followed=followed,
    )


@app.get("/account/<int:user_id>")
def get_followed_page(user_id):
    user = User.query.filter_by(id=user_id).first()

    current_user = session["user"]["user_id"]
    user_info = User.query.filter_by(id=current_user).first()

    followers_list = FollowedBy.query.filter_by(user_id=user_info.id).all()

    for followers in followers_list:
        if user_info.id == followers.user_id and user.id == followers.follower_id:
            followed = 1

    return render_template("pages/followed_page.html", user=user, followed=followed)


@app.post("/account/logout")
def log_out():
    if "user" not in session:
        return redirect("/landing")
    session.clear()
    return redirect("/landing")


@app.post("/account/unfollow")
def unfollow():
    if "user" not in session:
        return redirect("/landing")

    # gets follower id
    other_account_id = request.form.get("user")
    followed = User.query.filter_by(id=other_account_id).first()

    # gets session user id
    current_user = session["user"]["user_id"]
    user_info = User.query.filter_by(id=current_user).first()

    # gets folowers.
    followers_list = FollowedBy.query.filter_by(user_id=user_info.id).all()
    for followers in followers_list:
        if user_info.id == followers.user_id and followed == followers.follower_id:
            db.session.delete(followers)
            db.session.commit()
    return redirect("/account")


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
    return render_template("pages/sign_up_page.html", no_layout=True)


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

    session["user"] = {"user_id": confirm_user.id}
    return redirect("/")
    # rediret tot he correct page if everything checks out.


@app.get("/login")
def login_page():
    return render_template("pages/login.html", no_layout=True)
