from django.shortcuts import render
from django.http import HttpResponse

class Plant:
    def __init__(self, name, species, description, age):
        self.name = name
        self.species = species  # The type of plant, e.g., succulent, fern, etc.
        self.description = description  # Brief note about the plant
        self.age = age  # Plant's age in years or months

plants = [
    Plant('Sunny', 'Succulent', 'Thrives in bright sunlight.', 2),
    Plant('Fernie', 'Boston Fern', 'Loves humidity and shade.', 1),
    Plant('Spike', 'Cactus', 'Low-maintenance and drought-tolerant.', 3),
    Plant('Leafy', 'Monstera', 'Has large, beautiful leaves.', 4)
]

def home(request):
  return HttpResponse('<h1>Hello, plant collector</h1>')

def about(request):
  return render(request, 'about.html')

def plant_index(request):
  return render(request, 'plants/index.html',{ 'plants': plants } )