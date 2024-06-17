from django.shortcuts import render

# Create your views here.

from .models import Category, Program, Trainer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate


def home(request):
    categories = Category.objects.all()
    programs = Program.objects.all()
    trainers = Trainer.objects.all()
    return render(request, 'gym/home.html', {'categories': categories, 'programs': programs, 'trainers': trainers})

def program_detail(request, program_id):
    program = Program.objects.get(id=program_id)
    return render(request, 'gym/program_detail.html', {'program': program})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Adjust 'home' to your main landing page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Adjust 'home' to your main landing page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
