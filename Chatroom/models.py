from django.db import models
from posts.models import User
# Create your models here.
class ChatRoom(models.Model):
    # sender=models.ForeignKey(User,on_delete=models.CASCADE)
    sender=models.TextField()
    message=models.TextField() 

