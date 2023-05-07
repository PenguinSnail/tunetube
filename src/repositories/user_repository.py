from src.models import User, LikedBy

class UserInfo:
    def __init__(self, id, name, likes) -> None:
        self.id = id
        self.name = name
        self.likes = likes
        
    def getID(self):
        return self.id

    def getName(self):
        return self.name
    
    def isLiked(self, post_id):
        for post in self.likes:
            if post.getPost_id == post_id:
                return True
        return False               
    
class UserRepository:
    def get_user_info(self,username):
        user_id = User.query.filter_by(username = username).first().getID()
        likes =  LikedBy.query.filter_by(user_id = user_id)
        
        return UserInfo(user_id, username, likes)
    
# Singleton to be used in other modules
user_repository_singleton = UserRepository()