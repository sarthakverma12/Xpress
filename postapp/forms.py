from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PostUser
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit = True)
        puser = PostUser(user=user)
        puser.save()
        return user

class NewPostForm(forms.Form):
    image = forms.ImageField()
    caption = forms.CharField()
