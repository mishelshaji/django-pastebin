from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostCreationForm

# Create your views here.
@login_required
def home(request):
    # print(request.user.id)
    return render(request, 'user_home.html')

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