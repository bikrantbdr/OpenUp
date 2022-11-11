from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import  ModelForm
# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=1500)
    date_posted = models.DateTimeField(default=timezone.now)
    support = models.IntegerField()

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    age = models.IntegerField()
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length = 30)
    phone_number = models.IntegerField()
    anon_id = id 

    def __str__(self):
        return self.username


