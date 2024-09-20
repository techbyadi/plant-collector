from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('plants/', views.plant_index, name='plant-index'),
  path('plants/<int:plant_id>/', views.plant_detail, name='plant-detail'),
  path('plants/create/', views.PlantCreate.as_view(), name='plant-create'),
  path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plant-update'),
  path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant-delete'),
  path('plants/<int:plant_id>/add-watering/', views.add_watering, name='add-watering'),
  path('decorations/create/', views.DecorationCreate.as_view(), name='decoration-create'),
  path('decorations/<int:pk>/', views.DecorationDetail.as_view(), name='decoration-detail'),
  path('decorations/', views.DecorationList.as_view(), name='decoration-index'),
  path('decorations/<int:pk>/update/', views.DecorationUpdate.as_view(), name='decoration-update'),
  path('decorations/<int:pk>/delete/', views.DecorationDelete.as_view(), name='decoration-delete'),
  path('plants/<int:plant_id>/assoc-decoration/<int:decoration_id>/', views.assoc_decoration, name='assoc-decoration'),
  path('accounts/signup/', views.signup, name='signup'),
]