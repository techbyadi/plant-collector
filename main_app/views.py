from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Plant, Decoration
from .forms import WateringForm

# to be deleted code
plants_tbd = [
    Plant('Sunny', 'Succulent', 'Thrives in bright sunlight.', 2),
    Plant('Fernie', 'Boston Fern', 'Loves humidity and shade.', 1),
    Plant('Spike', 'Cactus', 'Low-maintenance and drought-tolerant.', 3),
    Plant('Leafy', 'Monstera', 'Has large, beautiful leaves.', 4)
]

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def plant_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html',{ 'plants': plants } )

@login_required
def plant_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  return render(request, 'plants/detail.html', {'plant': plant})

@login_required
def add_watering(request, plant_id):
  form = WateringForm(request.POST)
  if form.is_valid():
    new_watering = form.save(commit=False)
    new_watering.plant_id = plant_id
    new_watering.save()
  return redirect('plant-detail', plant_id=plant_id)


class PlantCreate(LoginRequiredMixin, CreateView):
  model = Plant
  fields = '__all__'

class PlantUpdate(LoginRequiredMixin, UpdateView):
  model = Plant
  fields = ['species', 'description', 'age']

class PlantDelete(LoginRequiredMixin, DeleteView):
  model= Plant
  success_url = '/plants/'

class DecorationCreate(LoginRequiredMixin, CreateView):
  model = Decoration
  fields = '__all__'

class DecorationList(LoginRequiredMixin, ListView):
  model = Decoration

class DecorationDetail(LoginRequiredMixin, DetailView):
  model = Decoration

class DecorationUpdate(LoginRequiredMixin, UpdateView):
  model = Decoration
  fields = ['name', 'color']

class DecorationDelete(LoginRequiredMixin, DeleteView):
  model = Decoration
  success_url = '/decorations/'

@login_required
def assoc_decoration(request, plant_id, decoration_id):
  Plant.objects.get(id=plant_id).toys.add(decoration_id)
  return redirect('plant-detail', plant_id=plant_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('plant-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)