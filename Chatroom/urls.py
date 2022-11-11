from django.urls import path

from . import views

# extends from chat/
urlpatterns = [
    path('', views.sendMsg, name = 'chat'),
    
]