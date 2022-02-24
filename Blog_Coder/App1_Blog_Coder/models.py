from email.policy import default
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Article(models.Model):
    
    title = models.CharField(max_length=50)
    content_resume = RichTextField(blank=True, null=True)
    content_upload = RichTextUploadingField(blank=True, null=True)
    publication_date = models.DateTimeField()
    picture = models.ImageField()
    author = models.CharField(max_length=30)
    
    def __str__(self):
        
        return f'{self.title}'
    
    
    
     
    