from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from App2_Login.forms import UserRegisterForm


# Create your views here.

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contrasena = form.cleaned_data['password']
            user = authenticate(username=usuario, password=contrasena)
            
            if user is not None:
                login(request, user)
                return redirect("app1_inicio")
        else:
            return render(request, "App2/login.html", {"form" : form,
                                                "error" : "Usuario y/o contraseña no válida"})
    else:
        form = AuthenticationForm()
        return render(request, "App2/login.html", {"form" : form})
    
def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "App2/_register.html")
    else:
        form = UserRegisterForm()
    
    return render(request, "App2/register.html", {'form':form})
