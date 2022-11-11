from django import forms
from .models import ChatRoom

class MessageForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = '__all__'