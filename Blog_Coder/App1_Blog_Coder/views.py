from django.http import HttpResponse
from django.shortcuts import redirect, render
from App1_Blog_Coder.models import Article
from App1_Blog_Coder.forms import ArticleForm


def inicio(request):
    
        
    return render(request, "App1/index.html")

def pages(request):
    
        
    return render(request, "App1/pages.html")

def about(request):
    
        
    return render(request, "App1/about.html")

def articulo(request):
    
    articles = Article.objects.all()
    
    return render(request, "App1/articulo1.html", {'articles':articles})

def detail(request):
    
    article = Article.objects.get(pk=1)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            
            return redirect('app1_detail')
    else:
        form = ArticleForm(instance=article)
    
    return render(request, "App1/detail.html", {'article':article, 'form':form})