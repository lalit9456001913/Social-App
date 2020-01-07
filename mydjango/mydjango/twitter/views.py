

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from twitter.forms import PostForm,LikedForm,DislikeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from twitter.models import Post,Liked,Dislike
from rest_framework.response import Response
from django.conf import settings
from django.core import serializers
from django.http import JsonResponse

from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.utils import timezone

def home(request):
    return render(request,'posts.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            request.session['username']=username
            return redirect('postpages')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        try:
            username=request.POST['username']
            raw_password=request.POST['password']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            request.session['username'] = username
            return redirect('postpages')
        except:
            return render(request,'registration/login.html')
    return render(request,'registration/login.html/')



def postpages(request):
    user = User.objects.filter(username=request.user)
    if user:

        if request.method=="GET":
            posts=Post.objects.all()
            return render(request,'posts.html',{'posts':posts})
        if request.method=="POST":
            form=PostForm(request.POST)
            if form.is_valid():
                post=form.save(commit=False)
                post.author=request.user
                post.published_date=timezone.now()
                post.created_date=timezone.now()
                post.likes=0
                post.dislikes=0
                post.save()
                return redirect('postpages')
            else:
                form=PostForm()
                return render(request,'newpost.html',{'form':form})
    else:
        return redirect('signin')




def likes(request):
    if request.method=="POST":
        form=LikedForm(request.POST)
        post_id=request.POST['post_id']
        post = Post.objects.get(post_id=post_id)
        user = User.objects.get(username=request.user)
        likes=Liked.objects.filter(post_id=post_id,user_id=user.id)
        if likes:
            return redirect('postpages')
        else:
            if form.is_valid():
                obj = form.save(commit=False)
                if Liked.objects.all()[:1] :
                    like=Liked.objects.all()[:1]
                    for i in like:
                        like_id=i.like_id+1
                else:
                        like_id=1
                post.likes = post.likes+ 1
                obj.like_id=like_id
                #obj.save()
                obj.post_id=post
                obj.user_id=user
                obj.save()
                post.save()
                return redirect('postpages')
            else:
                return redirect('postpages')
    else:
        return redirect('postpages')


def dislikes(request):
    if request.method == "POST":
        form = DislikeForm(request.POST)
        post_id = request.POST['post_id']
        post = Post.objects.get(post_id=post_id)
        user = User.objects.get(username=request.user)
        dislikes = Dislike.objects.filter(post_id=post_id, user_id=user.id)
        if dislikes:
            return redirect('postpages')
        else:
           if form.is_valid():
                obj = form.save(commit=False)
                if Dislike.objects.all()[:1]:
                    dislike = Dislike.objects.all()[:1]
                    for i in dislike:
                        dislike_id = i.dislike_id + 1
                else:
                    dislike_id = 1
                post.dislikes = post.dislikes + 1
                obj.dislike_id = dislike_id
                #obj.save()
                obj.post_id=post
                obj.user_id=user
                obj.save()
                post.save()
                return redirect('postpages')

           else:
                return redirect('postpages')
    else:
        return redirect('postpages')



def newpost(request):
    return render(request,'newpost.html')

def mylikes(request):
    user=User.objects.get(username=request.user)
    mylikes=Liked.objects.filter(user_id=user.id)
    return render(request,'likepost.html',{'mylikes':mylikes})

def myposts(request):
    user=User.objects.get(username=request.user)
    post=Post.objects.filter(author=user)
    return render(request,'myposts.html',{'posts':post})