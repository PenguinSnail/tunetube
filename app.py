import os
from dotenv import load_dotenv

from src.models import db, Post, User, Comment, LikedBy, FollowedBy
from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    request,
    session,
)
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


@app.route("/tunes/<int:post_id>", methods=["GET", "DELETE"])
def single_post(post_id: int):
    current_user = session["user"]["user_id"]
    user_info = user_repository_singleton.get_user_info(current_user)
    post_info = post_repository_singleton.get_post_info(post_id)

    if request.method == "DELETE":
        if post_info.post.user_id == user_info.getID():
            Post.query.filter_by(id=post_id).delete()
            db.session.commit()
        return ("", 204)

    return render_template(
        "pages/post_page.html",
        post_info=post_info,
        post=post_info.post,
        user_info=user_info,
    )


@app.route("/tunes/<int:post_id>/comments", methods=["POST"])
def comment_post(post_id: int):
    current_user = session["user"]["user_id"]

    comment = request.form.get("comment", "")

    if comment == "":
        pass

    new_comment = Comment(current_user, post_id, comment)
    db.session.add(new_comment)
    db.session.commit()
    pass

    return redirect(f"/tunes/{post_id}")


@app.route("/tunes/<int:post_id>/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(post_id: int, comment_id: int):
    current_user = session["user"]["user_id"]
    selected_comment = Comment.query.filter_by(id=comment_id)

    if selected_comment.first().user_id == current_user:
        selected_comment.delete()
        db.session.commit()
        return ("", 204)
    else:
        return ("", 403)


@app.route("/tunes/<int:post_id>/data", methods=["GET"])
def post_data(post_id: int):
    # Authentication
    if "user" not in session:
        return redirect("/landing")

    post_info = post_repository_singleton.get_post_info(post_id)

    return post_info.post.getSong()


@app.route("/tunes/<int:post_id>/like", methods=["POST", "DELETE"])
def like_action(post_id):
    current_user = session["user"]["user_id"]

    if request.method == "POST":
        new_like = LikedBy(current_user, post_id)
        db.session.add(new_like)
        db.session.commit()

    if request.method == "DELETE":
        LikedBy.query.filter_by(post_id=post_id, user_id=current_user).delete()
        db.session.commit()

    return ("", 204)


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


@app.route("/tunes", methods=["GET", "POST"])
def tunes_page():
    # Authentication
    if "user" not in session:
        return redirect("/landing")

    current_user = session["user"]["user_id"]

    if request.method == "POST":
        song = request.form.get("data")
        title = request.form.get("title")
        if song:
            post = Post(title=title, song=song, user_id=current_user)
            db.session.add(post)
            db.session.commit()
        return redirect("/tunes")

    user_posts = Post.query.filter_by(user_id=current_user)
    user_info = user_repository_singleton.get_user_info(current_user)

    return render_template(
        "pages/library_page.html",
        posts=user_posts,
        user_info=user_info,
        library_active=True,
    )


@app.get("/account")
def account_page():
    # Authentication
    if "user" not in session:
        return redirect("/landing")

    # get session user id
    current_user = session["user"]["user_id"]  # noqa
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
    followed = 0
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
    print(followed.id)

    # gets session user id
    current_user = session["user"]["user_id"]
    user_info = User.query.filter_by(id=current_user).first()
    print(user_info.id)

    # gets followers.
    followers_list = FollowedBy.query.filter_by(user_id=user_info.id).all()
    for followers in followers_list:
        if followers.follower_id == followed.id:
            db.session.delete(followers)
            db.session.commit()
    return redirect("/account")


@app.post("/account/follow")
def follow():
    if "user" not in session:
        return redirect("/landing")

    # gets follower id
    other_account_id = request.form.get("user")
    followed = User.query.filter_by(id=other_account_id).first()
    print(followed.id)

    # gets session user id
    current_user = session["user"]["user_id"]
    user_info = User.query.filter_by(id=current_user).first()
    print(user_info.id)

    # gets folowers.
    new_follow = FollowedBy(user_id=user_info.id, follower_id=followed.id)
    db.session.add(new_follow)
    db.session.commit()
    return redirect("/")


@app.route("/account/register", methods=["GET", "POST"])
def sign_up():
    error = None
    if request.method == "POST":  # actually making account
        name = request.form.get("name")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not password or not name or not confirm_password:
            error = "Please fill in all fields"

        if password != confirm_password:
            error = "Passwords must match"

        if User.query.filter(User.username.ilike(name)).first() is not None:
            error = "name already taken"

        hashed_password = bcrypt.generate_password_hash(password).decode()

        if not error:
            # creates new user
            user = User(username=name, password=hashed_password)
            db.session.add(user)
            db.session.commit()

            # logs you in
            session["user"] = {"user_id": user.id}

            # flashing before redirecting
            flash("you were successfully logged in!")
            return redirect("/")
        else:
            return render_template("pages/signup_page.html", error=error)

    # get request
    return render_template("pages/signup_page.html", no_layout=True)


@app.route("/login", methods=["GET", "POST"])
def login_info():
    error = None
    if request.method == "POST":  # actually logging in
        name = request.form.get("name")
        password = request.form.get("password")

        if not password or not name:
            error = "please fill in all fields"
            return render_template("pages/login_page.html", error=error)

        confirm_user = User.query.filter(User.username.ilike(name)).first()

        if not confirm_user:
            error = "user not found"
            return render_template("pages/login_page.html", error=error)

        if not bcrypt.check_password_hash(confirm_user.password, password):
            error = "incorrect password"
            return render_template("pages/login_page.html", error=error)

        session["user"] = {"user_id": confirm_user.id}
        flash("you were successfully logged in!")
        return redirect("/")
        # redirect tot he correct page if everything checks out.
    return render_template("pages/login_page.html", no_layout=True)
