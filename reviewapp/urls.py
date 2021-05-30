from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.register2, name='register2'),
    path('login', views.login2, name='login2'),
    path('feed', views.rviewfeed, name='rviewfeed'),
    path('addreview/<int:postid>', views.addreview, name='addreview'),
    path('writereview/<int:postid>', views.writereview, name='writereview'),
    path('viewreviews', views.viewreviews, name='viewreviews'),
    path('editreview/<int:reviewid>', views.editreview, name='editreview'),
    path('deletereview/<int:reviewid>', views.deletereview, name='deletereview'),

]