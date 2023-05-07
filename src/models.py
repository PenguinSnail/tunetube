from datetime import datetime , timezone 
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

class sharedMethods():
    def getUsername(self):
        return User.query.filter_by(id = self.user_id).first().getUsername()

    
class Photo(db.Model):
    id = db.Column(INTEGER, primary_key=True)
    photo = db.Column(BYTEA, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(VARCHAR(20), nullable=False)
    photo_id = db.Column(INTEGER, db.ForeignKey("photo.id"))
    password = db.Column(VARCHAR(127), nullable=False)

    
     # Constructor
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password


    # Getters and Setters
    def getUsername(self):
        return self.username
    
    def getPhotoID(self):
        return self.photo_id
    
    def setUsername(self,username):
        self.username = username
    
    def setUsername(self,photo_id):
        self.photo_id = photo_id
    

class Post(db.Model,sharedMethods):
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
    def getID(self):
        return self.id
    
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


class Comment(db.Model,sharedMethods):
    id = db.Column(INTEGER, primary_key=True)
    post_time = db.Column(TIMESTAMP, nullable=False)
    comment = db.Column(TEXT, nullable=False)
    post_id = db.Column(INTEGER, db.ForeignKey("post.id"), nullable=False)
    user_id = db.Column(INTEGER, db.ForeignKey("user.id"), nullable=False)
    
    def __init__(self,user_id,post_id,comment) -> None:
        self.user_id = user_id
        self.post_id = post_id
        self.comment = comment
        self.post_time = datetime.now(timezone.utc)
        
    def getID(self):
        return self.id
    
    def getPost_Time(self):
        return self.post_time 
    
    def show_Time(self):
        return self.post_time 
    
    def setPost_Time(self, time):
        self.post_time = time
        
    def getComment(self):
        return self.comment
    
    def setComment(self, comment):
        self.comment = comment
    
    def getPostID(self):
        return self.post_id
    
    def setPostID(self, id):
        self.post_id = id
    
    def getUserID(self):
        return self.post_id
    
    def setUserID(self, id):
        self.user_id = id

class LikedBy(db.Model):
    user_id = db.Column(
        INTEGER, db.ForeignKey("user.id"), primary_key=True, nullable=False
    )
    post_id = db.Column(
        INTEGER, db.ForeignKey("post.id"), primary_key=True, nullable=False
    )
    
    def __init__(self,user_id,post_id) -> None:
        self.post_id = post_id
        self.user_id = user_id
        
        
class FollowedBy(db.Model):
    user_id = db.Column(
        INTEGER, db.ForeignKey("user.id"), primary_key=True, nullable=False
    )
    follower_id = db.Column(
        INTEGER, db.ForeignKey("user.id"), primary_key=True, nullable=False
    )
