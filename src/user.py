from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    user_ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    photo_ID = db.Column(db.Integer, nullable=False)

    # Constructor
    def __init__(self, username, password, profile) -> None:
        self.username = username
        self.password = password
        self.photo_ID = profile

    # Getters and Setters
    def getUser_ID(self):
        return self.user_ID

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPhoto_ID(self):
        return self.photo_ID

    def setPhoto_ID(self, profile):
        self.photo_ID = profile

    def setPassword(self, password):
        self.password = password
