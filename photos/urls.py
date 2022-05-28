from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photo/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
]