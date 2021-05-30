from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ReviewUser
from django.contrib.auth.models import User

class NewReviewerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    def save(self, commit=True):
        user = super(NewReviewerForm, self).save(commit = True)
        puser = ReviewUser(user=user)
        puser.save()
        return user

class ReviewForm(forms.Form):
    rtext = forms.CharField(label='Review')