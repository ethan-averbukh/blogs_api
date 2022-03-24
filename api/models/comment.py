from django.db import models
from .blog import Blog
from .user import User

# content : string
# blog : blog reference
# author : user reference
# updated_at/created_at


class Comment(models.Model):

    content = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment: {self.content} from Blog: {self.blog}"