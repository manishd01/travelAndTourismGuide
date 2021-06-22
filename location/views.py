from django.shortcuts import render

# Create your views here.
def location(request):
    return render(request,'location.html')
    
def kangra(request):
    return render(request,'locations/kangra.html')

def una(request):
    return render(request,'locations/una.html')

def kullu(request):
    return render(request,'locations/kullu.html')

def chamba(request):
    return render(request,'locations/chamba.html')

def solan(request):
    return render(request,'locations/solan.html')

def sirmaur(request):
    return render(request,'locations/sirmaur.html')

def hamirpur(request):
    return render(request,'locations/hamirpur.html')

def kinnaur(request):
    return render(request,'locations/kinnaur.html')

def bilaspur(request):
    return render(request,'locations/bilaspur.html')

def lahul_spiti(request):
    return render(request,'locations/lahul_spiti.html')

def shimla(request):
    return render(request,'locations/shimla.html')

def mandi(request):
    return render(request,'locations/mandi.html')