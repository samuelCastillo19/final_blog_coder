from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Post(models.Model):
    title_blog = models.CharField(max_length=30)
    subtitle_blog = models.CharField(max_length=30)
    body = models.TextField()
    author = models.CharField(max_length=30)
    date = models.DateField()
    
class Article(models.Model):
    
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True, null=True)
    content_upload = RichTextUploadingField(blank=True, null=True)
    
    def __str__(self):
        
        return f'{self.title}'
    
    
    
     
    