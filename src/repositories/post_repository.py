from src.models import Post,Comment, db


class PostRepository:
    def get_post(self,id):
        post = Post.query.filer(Post.id.contains(id))
        return post
    
    def get_comments(self,post_id):
        comments = Comment.query.filer(Comment.post_id.contains(post_id))
        comments.sort()
        return comments

# Singleton to be used in other modules
post_repository_singleton = PostRepository()
