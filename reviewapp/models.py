from django.contrib.auth.models import User
from django.db import models
from postapp.models import Post
# Create your models here.

class ReviewUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(ReviewUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
