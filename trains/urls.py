from django.urls import path

from trains import views

urlpatterns = [
    path("trains-setting/",  views.TrainsIndex.as_view(), name="trains-setting"),
    path("trains-start/",  views.TrainsStart.as_view(), name="trains-start"),
]
