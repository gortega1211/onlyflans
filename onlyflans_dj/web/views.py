from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

PRODUCTS = [
    {"name": "Product1", "price": 10.5},
    {"name": "Product2", "price": 8.5},
    {"name": "Product3", "price": 5.0},
    {"name": "Product4", "price": 4.5}
]

def index(request):
    return render(request, "index.html", {"products": PRODUCTS})

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())

def welcome(request):
    client_name = f", {request.GET.get('clientName')}" if request.GET.get("clientName") else ", Dear client"
    template = loader.get_template("welcome.html")
    return HttpResponse(template.render({"client_name": client_name}))