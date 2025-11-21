from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def edu(request):
    return render(request, 'index.html')

def version1(request):
    return render(request, 'homepage_1.html')
