from django.shortcuts import render
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
    return render(request, 'user_new_post.html', {'form': PostCreationForm()})