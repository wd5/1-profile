from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=64, null=False)
    header = models.CharField(max_length=256, null=False)
    preview = models.TextField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=False)
    tag = models.CharField(max_length=32, null=False)

class Comment(models.Model):
    post = models.ForeignKey(Post, null=False)
    author = models.CharField(max_length=64, null=False)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    
