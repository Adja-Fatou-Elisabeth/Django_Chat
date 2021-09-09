from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, RedirectView, ListView,TemplateView, DeleteView
from django.urls import reverse

from .models import MessageChat
from .forms import MessageChatForm, ReponseChatForm

def index(request):
    return render(request, 'chatbot/index.html')

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = MessageChat.objects.filter(room=room_name)[0:25]

    return render(request, 'chatbot/room.html', {'room_name': room_name, 'username': username, 'messages': messages})

def message_liste(request):
    context ={}
    context["object_list"] = MessageChat.objects.all()
    return render(request, 'chatbot/message_liste.html',context)

def create_view(request):
    context ={}
 
    form = ReponseChatForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "reponse/create.html", context)

def list_view(request):
    context ={}
 
    context["object_list"] = ReponseChat.objects.all()
         
    return render(request, "reponse/liste.html", context)