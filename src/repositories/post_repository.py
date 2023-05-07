from src.models import Post,Comment, LikedBy, db

class SingularPostInfo:
    def __init__(self, post, comments, likes) -> None:
        self.post = post
        self.comments = comments
        self.likes = likes
        
    def getTitle(self):
        return self.post.getTitle()
    
    def getUsername(self):
        return self.post.getUsername()
    
    def getComments(self):
        return self.comments
    
    def getID(self):
        return self.post.getID()
    
    def likeCount(self):
        return self.likes.count()
    
class PostRepository:
    def get_post_info(self,post_id):
        post =  Post.query.filter_by(id = post_id).first()
        comments =  Comment.query.filter_by(post_id = post_id)
        likes =  LikedBy.query.filter_by(post_id=post_id)
        
        return SingularPostInfo(post, comments, likes)
    
# Singleton to be used in other modules
post_repository_singleton = PostRepository()
