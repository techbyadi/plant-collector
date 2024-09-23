from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plant_index, name='plant-index'),  # List all plants
    path('plants/<int:plant_id>/', views.plant_detail, name='plant-detail'),  # Show details of a single plant
    path('plants/create/', views.PlantCreate.as_view(), name='plant-create'),  # Create a new plant
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plant-update'),  # Update a plant
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant-delete'),  # Delete a plant
    path('plants/<int:plant_id>/add-watering/', views.add_watering, name='add-watering'),  # Add a watering to a plant
    path('decorations/create/', views.DecorationCreate.as_view(), name='decoration-create'),  # Create a decoration
    path('decorations/<int:pk>/', views.DecorationDetail.as_view(), name='decoration-detail'),  # Show a decoration detail
    path('decorations/', views.DecorationList.as_view(), name='decoration-index'),  # List all decorations
    path('decorations/<int:pk>/update/', views.DecorationUpdate.as_view(), name='decoration-update'),  # Update a decoration
    path('decorations/<int:pk>/delete/', views.DecorationDelete.as_view(), name='decoration-delete'),  # Delete a decoration
    path('plants/<int:plant_id>/assoc-decoration/<int:decoration_id>/', views.assoc_decoration, name='assoc-decoration'),  # Associate a decoration to a plant
    path('accounts/signup/', views.signup, name='signup'),  # Signup for a new user account
]
