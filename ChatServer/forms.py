from django import forms
from django.forms import ModelForm
from .models import ChatFormat

class ChatForm(forms.ModelForm):
    class meta:
        model= ChatFormat
        fields='__all__'