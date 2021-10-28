from django.http import request
from django.http.response import HttpResponse,HttpResponseRedirect
 
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Post
import datetime
# Create your views here.
def log(request): 
    return render(request,"users/login.html")





def handlelogin(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
         
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            user=request.user
            print("request.user:",request.user)
            if request.user.is_active:
                # return redirect('/login/')
                post=Post.objects.filter(user=user)
                return render(request,"users/posts.html",{"user":user,"post":post})
            if request.user.is_active:
                return HttpResponse("<h4> you are just an active member</h4>")

        else:
            return HttpResponse("<h4> invalid credentials !</h4>")

    else:
            return render(request,"users/login.html")


@login_required
def post(request):
    user=request.user
    if request.method=="POST":
        text=request.POST['post_text']
        crat=datetime.datetime.now()
        Post.objects.create(user=user,text=text,created_at=crat,updated_at=crat)
        post=Post.objects.filter(user=user)
    return render(request,"users/posts.html",{"user":user,"post":post})


@login_required
def handleupdatepost(request,id):
    user=request.user
    upt=Post.objects.get(id=id)
    if request.method =="POST":
        text=request.POST['post_text']
        # Post.objects.get(id=id).update(text=text)
        crat=datetime.datetime.now()
        upt.text=text
        upt.updated_at=crat
        upt.save()
        post=Post.objects.filter(user=user)
        return render(request,"users/posts.html",{"post":post,"user":user})

    return render(request,"users/updatepost.html",{"text":upt,"user":user})
