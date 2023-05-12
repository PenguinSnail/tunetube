from src.models import Comment, LikedBy, FollowedBy, Post, Photo, User, db
import json

def refresh_db():
    Comment.query.delete()
    LikedBy.query.delete()
    FollowedBy.query.delete()
    Post.query.delete()
    Photo.query.delete()
    User.query.delete()
    db.session.commit()

def create_user(username='tester', password='1234'):
    testing_user = User(username=username, password=password)
    db.session.add(testing_user)
    db.session.commit()
    return testing_user

def create_post(title='tempSong', song='{"time":702,"frequency":261.63,"playing":true}'):
   # song = json.loads(song)
    post = Post(title=title, song=song)
    db.session.add(post)
    db.session.commit()
