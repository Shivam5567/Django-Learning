from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/home.html')

def services(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/home.html')
