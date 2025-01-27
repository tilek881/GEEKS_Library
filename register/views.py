

from .models import Developer
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            experience = form.cleaned_data["experience"]
            salary = form.cleaned_data.get("salary", 0)
            Developer.objects.create(user=user, experience=experience, salary=salary)

            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "registation/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, name=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Неверный логин или пароль.")
    return render(request, "registation/login.html")
