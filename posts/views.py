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
    context = {} 
    if request.method == "POST":
        username = request.POST['username']
        #request.session['username'] = username
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            print("yess")
            return render(request, 'posts/questions.html', context)
    
    context = {'form':form} 
    return render(request, 'posts/register.html', context)



def login(request):

    if request.method == "POST":
        Username = request.POST['username']
        Password=request.POST['password']

        user_post = Post.objects.all()
        experts = Expert.objects.all()
        user_detail = User.objects.all()

        print(user_detail[0].username)
        for user in user_detail:
            
            if user.username == Username and user.password == Password:
                
                #return render(request,'posts/home.html',{'user': user})
                #set session:
                request.session['username'] = user.username
                
                return render(request, 'posts/mainpage.html',{'user': user, 'user_post': user_post,'experts':experts})
                
                
        # pop message wrong information message
        


    context = {}
    return render(request, 'posts/home.html', context)

def home(request):
    if request.method=="GET4":
        ans11=request.GET['ans']
        print(ans11)
        username = request.session['username']

        Disorder.objects.create(username= username, types= ans11 )    
            #message pop up already registered
            #return render(request,'register.html')
        return render(request,'posts/home.html')

    
    else:
        context = {} 
        return render(request, 'posts/home.html', context)

        



def forgotpassword(request):
    
    return render(request, 'posts/forgotpassword.html')


def makepost(request):
    if request.method=="POST":
        username = request.session['username']  
        #username="random"
        title = request.POST['title']
        content = request.POST['post_content']
        #print("makepost")
        
        user_post = Post.objects.all()
        experts = Expert.objects.all()
        user_detail = User.objects.all()

        for user in user_detail:
            
            if user.username == username:

        
                Post.objects.create(author= username, title=title,content = content,support = 0,report=0, comments_json={'available':0})    
                    #message pop up already registered
                    #return render(request,'register.html')
                return render(request,'posts/mainpage.html',{'user': user,'user_post': user_post,'experts':experts})

    
    else:
        context = {} 
        return render(request, 'posts/makepost.html', context)



def my_comment(request):
    username = request.session['username']
    user_post = Post.objects.all()
    return render(request, 'posts/mainpage.html',{'user_post': user_post})
  
def questions(request):
    print("hfudsih")
    return render(request, 'posts/questions.html')
