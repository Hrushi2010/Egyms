from django.shortcuts import render

# Create your views here.

from .models import Category, Program, Trainer

#def home(request):
  #  categories = Category.objects.all()
  #  programs = Program.objects.all()
  #  trainers = Trainer.objects.all()
   # return render(request, 'gym/home.html', {'categories': categories, 'programs': programs, 'trainers': trainers})

#def program_detail(request, program_id):
 #program = Program.objects.get(id=program_id)
 #   return render(request, 'gym/program_detail.html', {'program': program})

def index(request):
    return render(request, 'gym/index.html')

