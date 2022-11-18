from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')

def cv(request):
    return render(request, 'cv.html')

def contact(request):
    return render(request, 'contact-us.html')

def projects(request):
    return render(request, 'projects.html')

def aboutme(request):
    return render(request, 'about-me.html')