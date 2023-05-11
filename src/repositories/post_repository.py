from src.models import Post, Comment, LikedBy


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
    def get_post_info(self, post_id):
        post = Post.query.filter_by(id=post_id).first()
        comments = Comment.query.filter_by(post_id=post_id)
        likes = LikedBy.query.filter_by(post_id=post_id)

        return SingularPostInfo(post, comments, likes)

    def delete_post(self, post_id: int):
            """Delete a post"""
            # Make sure the post exists
            old_post = self.get_post_info
            # Complain if we did not find the post
            if not old_post:
                raise ValueError(f'post with id {post_id} not found')
            # Remove the post from the dict
            del self.post[post_id]

# Singleton to be used in other modules
post_repository_singleton = PostRepository()
