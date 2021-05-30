from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('addpost', views.addpost, name='addpost'),
    path('feed', views.viewfeed, name='viewfeed'),
    path('viewposts', views.viewposts, name = 'viewposts'),
    path('editpost/<int:postid>', views.editpost, name='editpost'),
    path('deletepost/<int:postid>', views.deletepost, name='deletepost'),
    path('postreviews/<int:postid>', views.postreviews, name='postreviews'),
]