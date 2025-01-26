from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home/index.html', {})

def log_in(request):
    if request.method =='GET':
        return render(request, 'home/login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.success(request, "El usuario no existe, o la password es incorrecta")
            return render(request, 'home/login.html', {'form': AuthenticationForm})
        else:
            login(request, user)
            return redirect('home')
        
@login_required
def log_out(request):
    logout(request)
    return redirect('home')        
