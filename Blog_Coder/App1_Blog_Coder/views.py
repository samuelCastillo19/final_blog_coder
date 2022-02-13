from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    
        
    return render(request, "App1/index.html")

def pages(request):
    
        
    return render(request, "App1/pages.html")

def about(request):
    
        
    return render(request, "App1/about.html")