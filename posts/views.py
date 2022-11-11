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
        Username = request.POST['username']
        Password=request.POST['password']
        user_detail = User.objects.all()
        for user in user_detail:
            
            if user.username == Username and user.password == Password:
                
                #return render(request,'posts/home.html',{'user': user})
                return render(request,'posts/home.html',{'user': user})
                
        # pop message wrong information message
        return render(request,'login.html')


    context = {}
    return render(request, 'posts/login.html', context)

def home(request, user):
    context = {
        'anon_id':user.anon_id,
    }
    return render(request, 'posts/home.html', context)

