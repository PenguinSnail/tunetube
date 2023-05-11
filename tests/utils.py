from src.models import Comment, LikedBy, FollowedBy, Post, Photo, User, db


def refresh_db():
    Comment.query.delete()
    LikedBy.query.delete()
    FollowedBy.query.delete()
    Post.query.delete()
    Photo.query.delete()
    User.query.delete()
    db.session.commit()
