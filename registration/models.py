from django.conf import settings
from django.db import models


# Create your models here.

class Post(models.Model):
    text = models.CharField(verbose_name='投稿', max_length=250)
    published_at = models.DateTimeField(verbose_name='投稿日',auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
