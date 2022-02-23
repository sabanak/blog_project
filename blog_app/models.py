from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.TextField()
    post_date=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-post_date',]

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
