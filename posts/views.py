from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
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
        print(user_detail[0].username)
        for user in user_detail:
            
            if user.username == Username and user.password == Password:
                
                #return render(request,'posts/home.html',{'user': user})
                #set session:
                request.session['username'] = user.username
                user_post = Post.objects.all()
                return render(request, 'posts/mainpage.html',{'user_post': user_post})
                
                
        # pop message wrong information message
        


    context = {}
    return render(request, 'posts/login.html', context)

def home(request):
    
    return render(request, 'posts/home.html')

def forgotpassword(request):
    
    return render(request, 'posts/forgotpassword.html')


def register(request):
    return render(request, 'posts/register.html')




def makepost(request):
    if request.method=="POST":
        username = request.session['username']  
        #username="random"
        title = request.POST['title']
        content = request.POST['post_content']
        
        
        Post.objects.create(author= username, title=title,content = content,support = 0,report=0, comments_json={'available':0})    
            #message pop up already registered
            #return render(request,'register.html')
        return render(request,'posts/makepost.html')

    
    else:
        context = {} 
        return render(request, 'posts/makepost.html', context)




