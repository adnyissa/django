from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # ganti 'home' sesuai URL utama
        else:
            return render(request, 'login.html', {'error': "Username atau password salah"})
    return render(request, 'login.html')
