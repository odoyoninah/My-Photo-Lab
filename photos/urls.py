from django.urls import path
from . import views

urlpatterns = [
    path('', views.image, name='image'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('addPhoto/', views.addPhoto, name='addPhoto'),
]