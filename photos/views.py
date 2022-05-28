from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def viewPhoto(request):
    return render(request, 'photo.html')

def addPhoto(request):
    return render(request, 'add.html')