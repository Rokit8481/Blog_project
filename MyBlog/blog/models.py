from django.db import models
from django.utils import timezone
from datetime import timedelta

class Author(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title
    
    def published_recently(self):
        return self.published_date >= timezone.now() - timedelta(days=7)