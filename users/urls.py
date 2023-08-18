
from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path("", views.index, name="index"),
    path("id/", views.id, name="id"),
    path("password/", views.password, name="password"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
]
