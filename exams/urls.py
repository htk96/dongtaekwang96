
from django.contrib import admin
from django.urls import path
from users import views
from exams import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("Information_Modification/", views.Information_Modification, name="Information_Modification"),
    path("Withdrawal/", views.Withdrawal, name="Withdrawal"),
    path("Word_Practice/", views.Word_Practice, name="Word_Practice"),
    path("Word_Practice_Set/", views.Word_Practice_Set, name="Word_Practice_Set"),
    path("Word_Test/", views.Word_Test, name="Word_Test"),
    path("Word_Test_History/", views.Word_Test_History, name="Word_Test_History"),
    path("Word_Test_Score/", views.Word_Test_Score, name="Word_Test_Score"),
    path("Word_Test_Set/", views.Word_Test_Set, name="Word_Test_Set"),
]