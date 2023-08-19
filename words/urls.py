from django.urls import path

from words import views

urlpatterns = [
    path("", views.WordList.as_view(), name="words"),
    path("word-input", views.WordInput.as_view(), name="word-input"),
]
