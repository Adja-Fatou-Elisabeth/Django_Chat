from django import forms  
from .models import  MessageChat


class MessageChatForm(forms.ModelForm):  
    class Meta:  
        model = MessageChat
        fields = "__all__"

