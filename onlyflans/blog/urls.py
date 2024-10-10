from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.blog_home, name="blog_home")
]