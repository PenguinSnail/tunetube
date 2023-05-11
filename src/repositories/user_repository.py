from src.models import User, LikedBy


class UserInfo:
    def __init__(self, user, likes) -> None:
        self.user = user
        self.likes = likes

    def getID(self):
        return self.user.getID()

    def getUsername(self):
        return self.user.getUsername()

    def isLiked(self, post_id):
        for post in self.likes:
            if post.getPost_ID() == post_id:
                return True
        return False


class UserRepository:
    def get_user_info(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        likes = LikedBy.query.filter_by(user_id=user_id)

        return UserInfo(user, likes)


# Singleton to be used in other modules
user_repository_singleton = UserRepository()
