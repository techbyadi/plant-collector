from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant

# to be deleted code
plants_tbd = [
    Plant('Sunny', 'Succulent', 'Thrives in bright sunlight.', 2),
    Plant('Fernie', 'Boston Fern', 'Loves humidity and shade.', 1),
    Plant('Spike', 'Cactus', 'Low-maintenance and drought-tolerant.', 3),
    Plant('Leafy', 'Monstera', 'Has large, beautiful leaves.', 4)
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def plant_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html',{ 'plants': plants } )

def plant_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  return render(request, 'plants/detail.html', {'plant': plant})

class PlantCreate(CreateView):
  model = Plant
  fields = '__all__'

class PlantUpdate(UpdateView):
  model = Plant
  fields = ['species', 'description', 'age']

class PlantDelete(DeleteView):
  model= Plant
  success_url = '/plants/'