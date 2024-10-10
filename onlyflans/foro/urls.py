from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.foro_home, name="foro_home")
]