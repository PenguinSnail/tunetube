from src.models import *

def refresh_db():
    Comment.query.delete()
    LikedBy.query.delete()
    FollowedBy.query.delete()
    Post.query.delete()
    Photo.query.delete()
    User.query.delete()
    db.session.commit()

    