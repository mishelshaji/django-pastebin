from django.contrib.auth.decorators import login_required
from django.forms.widgets import Select
from django.http import request
from django.http.response import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from user.models import Post
from markdown import Markdown

# Create your views here.
def home(request):
    data = Post.objects.all().order_by('-created_on')[:30]
    return render(request, 'home.html', {'data': data})

def about(request):
    return render(request, 'about.html')

def user_login(request):
    if request.method == "GET":
        # return render(request, 'login.html', {'form': AuthenticationForm()})
        return render(request, 'login.html', {'form': LoginForm()})
    
    # print(request.POST.get('username'))
    lf = LoginForm(request.POST)
    if lf.is_valid():
        username = lf.cleaned_data['username']
        password = lf.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('user_home')
        return render(request, 'login.html', {'form': lf, 'message': 'Invalid username or password'})
        
    return render(request, 'login.html', {'form': lf})

def register(request):
    if request.method == "GET":
        return render(request, 'register.html', {'form': UserCreationForm()})
    
    # If post
    ucf = UserCreationForm(request.POST)
    if ucf.is_valid():
        ucf.save()
        return redirect('login')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

def search(request):
    q = request.GET.get('s')
    if q:
        posts = Post.objects.filter(title__contains=q)
        # print(posts)

        total_posts = len(posts)
        if posts:
            res = {
                'query': q,
                'total_posts': total_posts,
                'posts': posts[:50],
            }
            return render(request, 'search.html', res)

        res = {
            "message": f"No results found for {q}",
        }
        return render(request, 'search.html', res)
        
    return render(request, 'search.html')

def view_post(request, id):
    try:
        post = Post.objects.get(pk=id)
        md = Markdown()
        html = md.convert(post.body)
        return render(request, 'post.html', {'data': post, 'rendered_post': html})
    except:
        return HttpResponseNotFound()