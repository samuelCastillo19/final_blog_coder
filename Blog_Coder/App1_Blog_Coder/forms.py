from django.forms import ModelForm
from App1_Blog_Coder.models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'