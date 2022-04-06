from django.contrib import admin
from .models import *

@admin.register(Laptop, Mobile)
class ViewAdmin(admin.ModelAdmin):
     pass
