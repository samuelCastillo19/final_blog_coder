from django.forms import ModelForm
from django import forms
from App1_Blog_Coder.models import Article

class ArticleForm(forms.Form):
    class Meta:
        model = Article
        fields = '__all__'
        
