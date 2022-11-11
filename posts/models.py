from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField()
    date_posted = models.DateTimeField(default=timezone.now)
    support = models.models.IntegerField()
