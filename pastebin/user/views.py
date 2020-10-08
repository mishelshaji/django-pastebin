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
    
    pcf = PostCreationForm(request.POST)
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
            p[0].delete()
        return redirect('user_home')