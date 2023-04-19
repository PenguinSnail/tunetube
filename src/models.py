from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import (
    BYTEA,
    INTEGER,
    JSONB,
    TEXT,
    TIMESTAMP,
    VARCHAR,
)


db = SQLAlchemy()


class Photo(db.Model):
    id = db.Column(INTEGER, primary_key=True)
    photo = db.Column(BYTEA, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(VARCHAR(20), nullable=False)
    photo_id = db.Column(INTEGER, db.ForeignKey("photo.id"))
    password = db.Column(VARCHAR(127), nullable=False)


class Post(db.Model):
    id = db.Column(INTEGER, primary_key=True)
    title = db.Column(VARCHAR(100), nullable=False)
    song = db.Column(JSONB, nullable=False)
    user_id = db.Column(INTEGER, db.ForeignKey("user.id"), nullable=False)


class Comment(db.Model):
    id = db.Column(INTEGER, primary_key=True)
    post_time = db.Column(TIMESTAMP, nullable=False)
    comment = db.Column(TEXT, nullable=False)
    post_id = db.Column(INTEGER, db.ForeignKey("post.id"), nullable=False)
    user_id = db.Column(INTEGER, db.ForeignKey("user.id"), nullable=False)


class LikedBy(db.Model):
    user_id = db.Column(
        INTEGER, db.ForeignKey("user.id"), primary_key=True, nullable=False
    )
    post_id = db.Column(
        INTEGER, db.ForeignKey("post.id"), primary_key=True, nullable=False
    )


class FollowedBy(db.Model):
    user_id = db.Column(
        INTEGER, db.ForeignKey("user.id"), primary_key=True, nullable=False
    )
    follower_id = db.Column(
        INTEGER, db.ForeignKey("user.id"), primary_key=True, nullable=False
    )
