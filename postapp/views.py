from django.shortcuts import render, redirect
from .forms import NewUserForm, NewPostForm
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .models import Post, PostUser
from django.contrib.auth.decorators import login_required
from reviewapp.models import Review
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        try:
            check = PostUser.objects.get(user=request.user)
            return redirect(reverse('viewfeed'))
        except:
            return redirect(reverse('rviewfeed'))
    if request.method=='GET':
        return render(request, 'index.html')
def register(request):
    if request.user.is_authenticated:
        try:
            check = PostUser.objects.get(user=request.user)
            return redirect(reverse('viewfeed'))
        except:
            return redirect(reverse('rviewfeed'))
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can login now!")
            return redirect("login")
        messages.error("There was some problem. Please try again!")
    else:
        form = NewUserForm()
    context = {'form': form}
    return render(request,'register.html', context)     

def login(request):
    if request.user.is_authenticated:
        try:
            check = PostUser.objects.get(user=request.user)
            return redirect(reverse('viewfeed'))
        except:
            return redirect(reverse('rviewfeed'))
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            try:
                check = PostUser.objects.get(user=user)
                auth_login(request, user)
                return redirect("viewfeed")
            except:
                pass
        messages.error(request, "Username or password wrong")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def addpost(request):
    try:
        check = PostUser.objects.get(user=request.user)
    except:
        return HttpResponse("You don't have permission to view this page")
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            caption = form.cleaned_data['caption']
            user = PostUser.objects.get(user=request.user)
            post = Post(user=user, image=image, caption=caption)
            post.save()
            return redirect(viewfeed)
    else:
        form = NewPostForm()
    return render(request, 'addpost.html', {'form': form})

@login_required
def viewfeed(request):
    try:
        check = PostUser.objects.get(user=request.user)
    except:
        return HttpResponse("You don't have permission to view this page")
    if request.method == 'GET':
        postlist = Post.objects.all()
        if len(postlist)==0:
          messages.error(request, "Nothing to show!!")
        return render(request, 'feed.html', {'postlist': postlist})


@login_required
def viewposts(request):
    try:
        check = PostUser.objects.get(user=request.user)
    except:
        return HttpResponse("You don't have permission to view this page")
    if request.method == 'GET':
        user = PostUser.objects.get(user=request.user)
        posts = Post.objects.filter(user=user)
        if len(posts)==0:
          messages.error(request, "Nothing to show!!")
        return render(request, 'myposts.html', {'posts': posts})

@login_required
def editpost(request, postid):
    try:
        check = PostUser.objects.get(user=request.user)
    except:
        return HttpResponse("You don't have permission to view this page")
    if request.method == 'GET':
        post = Post.objects.get(id=postid)
        data = { 'image': post.image, 'caption': post.caption}
        form = NewPostForm(initial = data)
        return render(request, 'editpost.html', {'form': form, 'post': post})
    if request.method == 'POST':
        post = Post.objects.get(id=postid)
        form = NewPostForm(request.POST, request.FILES)
        if form.data['image']:
            post.image = form.data['image']
        post.caption = form.data['caption']
        post.save()
        return redirect(viewposts)

@login_required
def deletepost(request, postid):
    try:
        check = PostUser.objects.get(user=request.user)
    except:
        return HttpResponse("You don't have permission to view this page")
    if request.method == 'GET':
        post = Post.objects.get(id=postid)
        post.delete()
        return redirect(viewposts)

@login_required
def postreviews(request, postid):
    if request.method == 'GET':
        post = Post.objects.get(id=postid)
        reviews = Review.objects.filter(post=post)
        if len(reviews)==0:
          messages.error(request, "No reviews found!!")
        try:
            check = PostUser.objects.get(user=request.user)
            return render(request, 'postreviews.html', {'reviews': reviews, 'post': post})
        except:
            return render(request, 'postreviews2.html', {'reviews': reviews, 'post': post})