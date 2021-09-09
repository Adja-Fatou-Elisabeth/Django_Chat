from django import forms  
from .models import  MessageChat, ReponseChat


class MessageChatForm(forms.ModelForm):  
    class Meta:  
        model = MessageChat
        fields = "__all__"


class ReponseChatForm(forms.ModelForm):  
    class Meta:  
        model = ReponseChat
        fields = "__all__"

