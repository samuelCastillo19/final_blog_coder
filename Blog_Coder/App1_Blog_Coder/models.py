from email.base64mime import body_decode
from django.db import models

class Post(models.Model):
    title_blog = models.CharField(max_length=30)
    subtitle_blog = models.CharField(max_length=30)
    body = models.TextField()
    author = models.CharField(max_length=30)
    date = models.DateField()
    
    
     
    