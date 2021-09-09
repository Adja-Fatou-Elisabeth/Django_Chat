from django.urls import path
from . import views



app_name = "chatbot"
urlpatterns = [
    path('', views.index, name='index'),
    path('liste/', views.message_liste, name='message'),
    path('reponse/', views.create_view, name='reponse'),
    path('<str:room_name>/', views.room, name='room'),

]
