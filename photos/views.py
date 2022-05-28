from multiprocessing import context
from django.shortcuts import render
from .models import Category, Photo


def index(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'index.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo': photo})

def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        new_photo = Photo(description=request.POST['description'], image=request.FILES['image'], category=Category.objects.get(id=request.POST['category']))
        new_photo.save()
        return render(request, 'index.html', {'categories': categories})
    context = {'categories': categories}
    return render(request, 'add.html', context)