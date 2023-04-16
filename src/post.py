from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):
    post_ID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    song = db.Column(db.jsonb, nullable=False)
    user_ID = db.Column(db.Integer, nullable=False)

    # Constructor
    def __init__(self, title, song, user_ID) -> None:
        self.title = title
        self.song = song
        self.user_ID = user_ID

    # Getters and Setters
    def getPost_ID(self):
        return self.post_ID

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getSong(self):
        return self.song

    def setSong(self, song):
        self.song = song

    def getUser_ID(self):
        return self.user_ID

    def setUser_ID(self, user_ID):
        self.user_ID = user_ID
