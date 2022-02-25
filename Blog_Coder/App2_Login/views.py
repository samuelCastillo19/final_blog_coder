from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from App2_Login.forms import UserRegisterForm, UserEditForm


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

@login_required
def editar_perfil(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data['email']
            usuario.set_password(data['password1'])
            usuario.save()
            return redirect('app1_inicio')
    else:
        formulario = UserEditForm({'email': usuario.email})
        
    return render(request, 'App2/editar_perfil.html', {'form': formulario})
