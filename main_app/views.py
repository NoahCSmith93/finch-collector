from django.shortcuts import render
from .models import Finch
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# finches = [
#   {'name': 'Twitter', 'species': 'Blue Finch', 'description': 'A classic for all ages!', 'age': 14},
#   {'name': 'Chi', 'species': 'St Lucia Black Finch', 'description': 'People dont seem to like this one as much...', 'age': 1},
# ]

# Create your views here.
def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def finches_index (request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

class FinchesDetail(DetailView):
    model = Finch

class FinchesCreate(CreateView):
    model = Finch
    fields = ['species', 'habitat', 'description']

class FinchesUpdate(UpdateView):
    model = Finch
    fields = ['species', 'habitat', 'description']

class FinchesDelete(DeleteView):
    model = Finch
    success_url = '/finches'