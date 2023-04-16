from flask import Flask, render_template
from src.repositories.post_repository import post_repository_singleton


app = Flask(__name__)


# get's usuer ID to create feed
@app.get("/user_ID")
def index(user_ID):
    feed = post_repository_singleton.get_user_feed(user_ID)
    return render_template("index.html", home_active=True, feed=feed)


# gets a specific post from the feed
@app.get("/post/<int:post_id>")
def get_single_post(post_id):
    single_post = post_repository_singleton.get_post_by_id(post_id)
    return render_template("post.html", home_active=True, post=single_post)
