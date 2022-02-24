from django.urls import reverse_lazy
from django.shortcuts import render
from App1_Blog_Coder.models import Article
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView


def inicio(request):
    
        
    return render(request, "App1/index.html")

# def pages(request):
    
#     articles = Article.objects.all()
    
    
#     return render(request, "App1/pages.html", {'articles':articles})

def about(request):
    
        
    return render(request, "App1/about.html")

# def detail(request, id_article):
    
#     article = Article.objects.get(id=id_article)
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             return redirect('app1_articulos')
#     else:
#         form = ArticleForm(model_to_dict(article))
    
#     return render(request, "App1/detail.html", {'article':article, 'form':form, 'id_article':id_article})

class ArticleListView(ListView):
    model = Article
    template_name = 'App1/pages.html'
    context_object_name = 'articles'
class ArticleUpdateView(UpdateView):
    model = Article
    success_url = reverse_lazy('app1_articulos')
    fields = ['title', 'content_resume', 'content_upload', 'publication_date', 'picture', 'author']    
    template_name = "App1/update_article.html"

class ArticleCreateView(CreateView):
    model = Article
    success_url = reverse_lazy('app1_pages')
    fields = ['title', 'content_resume', 'content_upload', 'publication_date', 'author']    
    template_name = "App1/new_article.html"
    
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('app1_pages')
    template_name = "App1/delete_article.html"
    context_object_name = 'articles'
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = "App1/detail_article.html"
    
