from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request, "index.html", {})

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())

def welcome(request):
    template = loader.get_template("welcome.html")
    return HttpResponse(template.render())