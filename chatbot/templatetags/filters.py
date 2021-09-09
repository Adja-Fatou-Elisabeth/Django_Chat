from django import template
from chatbot.models import MessageChat,ReponseChat
register = template.Library()

def reponse_listes(value):
    try:
        return value.reponsechat_set.all()
    except ReponseChat.DoesNotExist:
        return []


register.filter('reponse_listes', reponse_listes)