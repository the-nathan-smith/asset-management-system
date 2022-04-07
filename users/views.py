from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from inventory.models import Laptop, Mobile
from .forms import RegisterUserForm, EditProfileForm


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Successfully logged in."))
            return redirect("index")
        else:
            messages.success(request, ("There was an error loggin in, try again..."))
            return redirect("login")
    else:
        return render(request, "authenticate/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully logged out."))
    return redirect("index")


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Account successfully registered!."))
            return redirect("index")
    else:
        form = RegisterUserForm()

    return render(request, "authenticate/register_user.html", {"form": form})


def display_profile(request):
    laptops = Laptop.objects.all()
    mobiles = Mobile.objects.all()
    date_joined = request.user.date_joined.strftime("%d %b %Y")
    context = {
        "user": request.user,
        "date_joined": date_joined,
        "laptops": laptops,
        "mobiles": mobiles,
    }

    return render(request, "authenticate/display_profile.html", context)


def edit_profile(request):
    if request.method == "POST":
        edit_profile_form = EditProfileForm(request.POST, instance=request.user)

        if edit_profile_form.is_valid():
            edit_profile_form.save()
            messages.success(request, "Your profile is updated successfully")
            return redirect("display_profile")
    else:
        edit_profile_form = EditProfileForm(instance=request.user)

    return render(
        request, "authenticate/edit_profile.html", {"form": edit_profile_form}
    )
