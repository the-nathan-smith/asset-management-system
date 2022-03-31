from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^login_user$", views.login_user, name="login"),
    re_path(r"^logout_user$", views.logout_user, name="logout"),
    re_path(r"^register_user$", views.register_user, name="register_user"),
]
