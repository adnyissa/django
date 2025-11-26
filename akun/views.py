from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index_view(request):
    return render(request, 'index.html')  # menampilkan index.html

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # setelah login, redirect ke index
        else:
            return render(request, 'login.html', {'error': "Username atau password salah"})
    return render(request, 'login.html')
