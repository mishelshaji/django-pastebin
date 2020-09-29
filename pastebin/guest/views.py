from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == "GET":
        # return render(request, 'login.html', {'form': AuthenticationForm()})
        return render(request, 'login.html', {'form': LoginForm()})
    
    # print(request.POST.get('email'))
    lf = LoginForm(request.POST)
    if lf.is_valid():
        return HttpResponse("Welcome")
    return render(request, 'login.html', {'form': lf})

def register(request):
    if request.method == "GET":
        return render(request, 'register.html', {'form': UserCreationForm()})
    
    # If post
    ucf = UserCreationForm(request.POST)
    if ucf.is_valid():
        ucf.save()
        return redirect('login')