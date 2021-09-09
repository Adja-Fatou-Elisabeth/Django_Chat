from django.db import models

# Create your models here.


class MessageChat(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


    class Meta:
        ordering = ('date_added',)





class ReponseChat(models.Model):
    username = models.CharField(max_length=255)
    mes = models.ForeignKey(MessageChat, on_delete=models.CASCADE)
    reponse = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reponse

    class Meta:
        ordering = ('date_added',)
