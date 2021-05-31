from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PostUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Post(models.Model):
    user = models.ForeignKey(PostUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts', blank = False)
    caption = models.CharField(max_length=200)
