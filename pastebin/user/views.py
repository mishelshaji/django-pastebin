import os
from django.http.response import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostCreationForm
from .models import Post

# Create your views here.
@login_required
def home(request):
    data = Post.objects.filter(created_by=request.user).order_by('-created_on')
    return render(request, 'user_home.html', {'data': data})

@login_required
def new_post(request):
    if request.method == "GET":
        return render(request, 'user_new_post.html', {'form': PostCreationForm()})
    
    pcf = PostCreationForm(request.POST, request.FILES)
    if pcf.is_valid():
        # print(request.user.id)
        post = pcf.save(commit=False)
        post.created_by = request.user

        post.save()
        return redirect('user_home')
    return render(request, 'user_new_post.html', {'form': pcf})

@login_required
def delete_post(request, id):
    if request.method == "GET":
        p = Post.objects.filter(id=id, created_by=request.user)
        if p:
            post = p[0]
            if post.featured_image:
                if os.path.isfile(post.featured_image.path):
                    os.remove(post.featured_image.path)
            post.delete()
        return redirect('user_home')

@login_required
def edit_post(request, id):
    p = Post.objects.filter(id=id, created_by=request.user)
    if p is None:
        return HttpResponseNotFound()

    if request.method == "GET":
        print(p[0])
        pcf = PostCreationForm(instance=p[0])
        return render(request, 'user_edit_post.html', {'form': pcf})
        
    # If the request method id POST
    pcf = PostCreationForm(data = request.POST, files= request.FILES, instance=p[0])
    if pcf.is_valid():
        pcf.save()
        return redirect('user_home')
    return render(request, 'user_edit_post.html', {'form': pcf})
