from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'regster'),
    path('login', views.login, name = 'login'),
    path('home', views.home, name = 'home'),
    path('makepost', views.makepost, name = 'makepost'),


    path('forgotpassword', views.forgotpassword, name = 'forgotpassword'),
    path('register', views.register, name = 'register'),
    path('my_comment', views.my_comment, name = 'my_comment'),
    path('questions', views.questions, name = 'questions'),

]