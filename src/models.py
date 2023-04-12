from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_name = db.Column(db.String(255), nullable=False)
    song = db.Column(db.JSON, nullable=False)
    creator = db.Column(db.Integer, nullable=False)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    photoID = db.Column(db.Integer, db.ForeignKey("photoID"))
