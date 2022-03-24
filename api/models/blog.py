from django.utils import timezone
from django.db import models
from .user import User

class Blog(models.Model):

    title = models.CharField(max_length=255, unique=True)
    content = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Blog post: '{self.title}': {self.content}. Written By {self.author}"