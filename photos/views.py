from django.shortcuts import render


def index(request):
    return render(request, 'photos/index.html')

def viewPhoto(request, pk):
    return render(request, 'photos/photo.html')

def addPhoto(request):
    return render(request, 'photos/form.html')