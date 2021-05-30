from django.shortcuts import render, redirect
from .forms import NewReviewerForm, ReviewForm
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from postapp.models import Post
from django.contrib.auth.decorators import login_required
from .models import Review, ReviewUser
# Create your views here.

def register2(request):
    if request.method == 'POST':
        form = NewReviewerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can login now!")
            return redirect("login2")
        messages.error("There was some problem. Please try again!")
    else:
        form = NewReviewerForm()
    context = {'form': form}
    return render(request,'register2.html', context)     

def login2(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            try:
                check = ReviewUser.objects.get(user=user)
                auth_login(request, user)
                return redirect("rviewfeed")
            except:
                pass
        messages.error(request, "Username or password wrong")
    else:
        form = AuthenticationForm()
    return render(request, 'login2.html', {'form': form})

@login_required
def rviewfeed(request):
    try:
        check = ReviewUser.objects.get(user=request.user)
    except:
        return HttpResponse("You don't have permission to view this page")
    if request.method == 'GET':
        postlist = Post.objects.all()
        if len(postlist)==0:
          messages.error(request, "Nothing to show!!")
        return render(request, 'rfeed.html', {'postlist': postlist})

@login_required
def addreview(request, postid):
    try:
        check = ReviewUser.objects.get(user=request.user)
    except:
        return HttpResponse("You don't have permission to view this page")
    if request.method == 'GET':
        post = Post.objects.get(id=postid)
        form = ReviewForm()
        return render(request, 'review.html', {'post': post, 'form': form})

@login_required
def writereview(request, postid):
    try:
        check = ReviewUser.objects.get(user=request.user)
    except:
        return HttpResponse("You don't have permission to view this page")
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
           post = Post.objects.get(id=postid)
           rtext = form.cleaned_data['rtext']
           user = ReviewUser.objects.get(user=request.user)
           review = Review(user=user, post=post, text=rtext)
           review.save()
           return redirect(viewreviews)

@login_required
def viewreviews(request):
    try:
        check = ReviewUser.objects.get(user=request.user)
    except:
        return HttpResponse("You don't have permission to view this page")
    if request.method == 'GET':
        user = ReviewUser.objects.get(user=request.user)
        reviews = Review.objects.filter(user=user)
        if len(reviews)==0:
          messages.error(request, "You haven't reviewed any post yet!!")
        return render(request, 'myreviews.html', {'reviews': reviews})

@login_required
def editreview(request, reviewid):
    try:
        check = ReviewUser.objects.get(user=request.user)
    except:
        return HttpResponse("You don't have permission to view this page")
    if request.method == 'GET':
        review = Review.objects.get(id=reviewid)
        data = {'rtext': review.text}
        form = ReviewForm(initial = data)
        return render(request, 'editreview.html', {'form': form, 'review': review})
    if request.method == 'POST':
        review = Review.objects.get(id=reviewid)
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review.text = form.cleaned_data['rtext']
            review.save()
            return redirect(viewreviews)


@login_required
def deletereview(request, reviewid):
    try:
        check = ReviewUser.objects.get(user=request.user)
    except:
        return HttpResponse("You don't have permission to view this page")
    if request.method == 'GET':
        review = Review.objects.get(id=reviewid)
        review.delete()
        return redirect(viewreviews)