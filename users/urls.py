from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^login_user$', views.login_user, name='login'),
]
