from multiprocessing import context
from django.shortcuts import render
from .models import Category, Photo


def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'index.html', context)

def viewPhoto(request, pk):
    return render(request, 'photo.html')

def addPhoto(request):
    return render(request, 'add.html')