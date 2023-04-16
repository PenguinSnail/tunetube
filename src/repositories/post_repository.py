from src.models import Post, db


class PostRepository:
    def get_post(self,id):
        post = Post.query.filer(Post.id.contains(id))
        return post

# Singleton to be used in other modules
post_repository_singleton = PostRepository()
