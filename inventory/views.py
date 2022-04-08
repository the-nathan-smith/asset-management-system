from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from inventory.forms import *
from .models import *


def index(request):
    context = {"header": "Home"}
    return render(request, "inventory/index.html", context)


# Passes a list of all laptop objects to the template
def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        "items": items,
        "header": "Laptops",
    }
    return render(request, "inventory/index.html", context)


# Passes a list of all mobile objects to the template
def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        "items": items,
        "header": "Mobiles",
    }
    return render(request, "inventory/index.html", context)


# This function reduces code duplication and is used to add both
# laptops and mobile devices
def add_device(request, deviceForm):
    if request.method == "POST":
        form = deviceForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, ("Device added successfully."))
            return redirect("index")

    else:
        form = deviceForm()
        return render(request, "inventory/add_new.html", {"form": form})


def add_laptop(request):
    return add_device(request, LaptopForm)


def add_mobile(request):
    return add_device(request, MobileForm)


# Similar to add_device this function reduces code duplication
# as it is used to edit both laptops and mobiles
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


def delete_device(request, model, pk, deviceType):
    model.objects.filter(id=pk).delete()
    items = model.objects.all()
    context = {"items": items, "header": deviceType}
    messages.success(request, ("Device successfully deleted."))

    return render(request, "inventory/index.html", context)


def delete_laptop(request, pk):
    return delete_device(request, Laptop, pk, "Laptops")


def delete_mobile(request, pk):
    return delete_device(request, Mobile, pk, "Mobiles")
