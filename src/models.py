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
    
     # Constructor
    def __init__(self,username,photo_id) -> None:
        self.username = username
        self.photo_id = photo_id

    # Getters and Setters
    def getUsername(self):
        return self.username
    
    def getPhotoID(self):
        return self.photo_id
    
    def setUsername(self,username):
        self.username = username
    
    def setUsername(self,photo_id):
        self.photo_id = photo_id
    

class Post(db.Model):
    id = db.Column(INTEGER, primary_key=True)
    title = db.Column(VARCHAR(100), nullable=False)
    song = db.Column(JSONB, nullable=False)
    user_id = db.Column(INTEGER, db.ForeignKey("user.id"), nullable=False)
    
    # Constructor
    def __init__(self,title,song,user_id) -> None:
        self.title = title
        self.song = song
        self.user_id = user_id

    # Getters and Setters
    def getTitle(self):
        return self.title
    
    def getSong(self):
        return self.song
    
    def getUserID(self):
        return self.user_id

    def setTitle(self, title):
        self.tile = title
    
    def setSong(self,song):
        self.song = song
    
    def setUserID(self,user_id):
        self.user_id = user_id


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
