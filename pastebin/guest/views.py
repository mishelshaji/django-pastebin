from django.shortcuts import render, HttpResponse
from .forms import LoginForm
# from django.contrib.auth.forms import AuthenticationForm

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