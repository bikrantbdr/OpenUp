from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
def index(request):
    return HttpResponse("Hello Django from Hackathon")

def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        context = {'form':form} 
        return render(request, 'posts/register.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        temp = User.objects.filter_by(username = username)
        if(password==temp.password):
            redirect('posts/home.html')
            

        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'posts/login.html', context)

def home(request, user_id):
    context = {
        'user_id':user_id,
    }
    return render(request, 'posts/home.html', context)

