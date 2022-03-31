from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from inventory.forms import *
from .models import *


def index(request):
    context = {"header": "Home"}
    return render(request, "inventory/index.html", context)


def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        "items": items,
        "header": "Laptops",
    }
    return render(request, "inventory/index.html", context)


def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        "items": items,
        "header": "Mobiles",
    }
    return render(request, "inventory/index.html", context)


def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = cls()
        return render(request, "inventory/add_new.html", {"form": form})


def add_laptop(request):
    return add_device(request, LaptopForm)


def add_mobile(request):
    return add_device(request, MobileForm)


def edit_device(request, pk, model, form, deviceType):
    item = get_object_or_404(model, pk=pk)
    items = model.objects.all()
    context = {"items": items, "header": deviceType}

    if request.method == "POST":
        form = form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ("Device edited successfully."))
            return render(request, "inventory/index.html", context)

    else:
        form = form(instance=item)
        return render(request, "inventory/edit_item.html", {"form": form})


def edit_laptop(request, pk):
    deviceType = "Laptops"
    return edit_device(request, pk, Laptop, LaptopForm, deviceType)


def edit_mobile(request, pk):
    deviceType = "Mobiles"
    return edit_device(request, pk, Mobile, MobileForm, deviceType)


def delete_laptop(request, pk):
    Laptop.objects.filter(id=pk).delete()
    items = Laptop.objects.all()
    context = {"items": items, "header": "Laptops"}
    messages.success(request, ("Device successfully deleted."))

    return render(request, "inventory/index.html", context)


def delete_mobile(request, pk):
    Mobile.objects.filter(id=pk).delete()
    items = Mobile.objects.all()
    context = {"items": items, "header": "Mobiles"}
    messages.success(request, ("Device successfully deleted."))

    return render(request, "inventory/index.html", context)
