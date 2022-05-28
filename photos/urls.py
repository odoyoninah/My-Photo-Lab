from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('addPhoto/', views.addPhoto, name='addPhoto'),
]