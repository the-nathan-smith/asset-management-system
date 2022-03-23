from django.shortcuts import redirect, render

from inventory.forms import *
from .models import *

def index(request):
    return render(request, 'index.html')


def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items' : items,
        'header' : 'Laptops',
    }
    return render(request, 'index.html', context)


def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items' : items,
        'header' : 'Mobiles',
    }
    return render(request, 'index.html', context)


def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else :
        form = cls()
        return render(request, 'add_new.html', {'form': form})


def add_laptop(request):
    return add_device(request, LaptopForm)


def add_mobile(request):
    return add_device(request, MobileForm)
