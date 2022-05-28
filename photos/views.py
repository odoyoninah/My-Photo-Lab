from django.shortcuts import render

# Create your views here.

def image(request):
    return render(request, 'photos/image.html')

def viewPhoto(request, pk):
    return render(request, 'photos/photo.html')

def addPhoto(request):
    return render(request, 'photos/form.html')