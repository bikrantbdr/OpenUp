from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'regster'),
    path('login', views.login_page, name = 'login'),
    path('home', views.home, name = 'home'),
]