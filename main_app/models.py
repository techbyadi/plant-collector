from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TIME = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Decoration(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("decoration-detail", kwargs={"pk": self.id})

class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    decorations = models.ManyToManyField(Decoration)  # Add ManyToManyField for decorations
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add ForeignKey for user

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plant-detail', kwargs={'plant_id': self.id})

    def fed_for_today(self):
        return self.watering_set.filter(date=date.today()).count() >= len(TIME)  # Ensure watering logic matches feeding logic

class Watering(models.Model):
    date = models.DateField('Watering date')  # Rename to Watering date
    time = models.CharField(
        max_length=1,
        choices=TIME,
        default=TIME[0][0]
    )
    
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
