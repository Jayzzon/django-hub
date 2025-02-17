from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {
    })

def servicios(request):
    return render(request, 'servicios.html', {
    })


# Create your views here.
