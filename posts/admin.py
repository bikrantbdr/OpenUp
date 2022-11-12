from django.contrib import admin
from .models import User, Post, Disorder, Expert
# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Disorder)
admin.site.register(Expert)