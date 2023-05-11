import os
from dotenv import load_dotenv

from src.models import db, Post, User, Comment, LikedBy
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


@app.route("/tunes/<int:post_id>", methods=["GET"])
def single_post(post_id: int):
    current_user = session["user"]["user_id"]
    user_info = user_repository_singleton.get_user_info(current_user)

    post_info = post_repository_singleton.get_post_info(post_id)
    return render_template(
        "pages/post_page.html",
        post_info=post_info,
        post=post_info.post,
        user_info=user_info,
    )


@app.route("/tunes/<int:post_id>/comment", methods=["POST"])
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


@app.get("/tunes")
def library_page():
    # Authentication
    if "user" not in session:
        return redirect("/landing")
    current_user = session["user"]["user_id"]

    user_posts = Post.query.filter_by(user_id=current_user)
    user_info = user_repository_singleton.get_user_info(current_user)

    return render_template(
        "pages/library_page.html",
        posts=user_posts,
        user_info=user_info,
        library_active=True,
    )


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

    return render_template("pages/account_page.html", account_active=True)


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
            return render_template("pages/login.html", error=error)

        if not bcrypt.check_password_hash(confirm_user.password, password):
            error = "incorrect password"
            return render_template("pages/login.html", error=error)

        session["user"] = {"user_id": confirm_user.id}
        flash("you were successfully logged in!")
        return redirect("/")
        # redirect tot he correct page if everything checks out.
    return render_template("pages/login_page.html", no_layout=True)

@app.post('/library_page/<int:id>/delete')
def delete_post(post_id: int):
    post_repository_singleton.delete_post(post_id)
    return redirect('/library_page')
