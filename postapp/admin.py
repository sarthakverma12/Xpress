from django.contrib import admin
from .models import Post, PostUser
# Register your models here.
admin.site.register(Post)
admin.site.register(PostUser)