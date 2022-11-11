from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ChatRoom
from .forms import MessageForm
# Create your views here.

def sendMsg(request):
    form=MessageForm()
    if(request.method=="POST"):
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'ChatRoom/msg.html',context={'form':form})
        else:
            #redirect ("../../../posts/templates/posts/home.html")

            #return render(request,"ChatRoom/msg.html",context={'form':form})
            return HttpResponse("<p> hello</P>")
    else:
        return render(request,'ChatRoom/msg.html',context={'form':form})

def baseView(request):
    form=MessageForm()
    