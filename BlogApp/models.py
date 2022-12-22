from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #From Django's default user and auth system

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now) #on post creation, the default date and time in the timzeone will be set for the post.
    author = models.ForeignKey(User, on_delete=models.CASCADE) #User will have a one-many relation with Post
    
    def __str__(self):
        return self.title 
