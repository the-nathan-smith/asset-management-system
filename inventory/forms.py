from django import forms

from .models import *


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ("type", "owner", "status")


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ("type", "owner", "status")
