from django.shortcuts import render

def peserta_dashboard(request):
    return render(request, 'peserta.html')
