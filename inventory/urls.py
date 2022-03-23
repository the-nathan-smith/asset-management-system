from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^display_laptops$', display_laptops, name='display_laptops'),
    re_path(r'^display_mobiles$', display_mobiles, name='display_mobiles'),

    re_path(r'^add_laptop$', add_laptop, name='add_laptop'),
    re_path(r'^add_mobile$', add_mobile, name='add_mobile'),
]
