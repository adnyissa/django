from django.shortcuts import render

def mentor_dashboard(request):
    return render(request, 'mentor.html')
