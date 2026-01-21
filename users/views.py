from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from .forms import RegisterForm, LoginForm
from .models import Profile


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})

    elif request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data.pop("confirm_password")
            age = form.cleaned_data.pop("age")
            photo = form.cleaned_data.pop("photo")
            user = User.objects.create_user(**form.cleaned_data)
            if user:
                Profile.objects.create(user=user, age=age, photo=photo)
                login(request, user)
                return redirect("/")

        return HttpResponse("Invalid register form")


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)
                return redirect("/")
        return HttpResponse("Invalid login data")


@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect("/")



@login_required(login_url="/login/")
def profile_view(request):
    user = request.user
    return render(request, "users/profile.html", {"user": user, "products": products})
