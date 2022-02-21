from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
    
class Article(models.Model):
    
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True, null=True)
    content_upload = RichTextUploadingField(blank=True, null=True)
    
    def __str__(self):
        
        return f'{self.title}'
    
    
    
     
    