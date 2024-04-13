from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

PRODUCTS = [
    {"id": 1, "name": "Product1", "price": 10.5, "picture": "https://picsum.photos/seed/picsum/200/300", "description": "Product's description 1"},
    {"id": 2, "name": "Product2", "price": 8.5, "picture": "https://picsum.photos/id/237/200/300", "description": "Product's description 2"},
    {"id": 3, "name": "Product3", "price": 5.0, "picture": "https://picsum.photos/200/300?grayscale", "description": "Product's description 3"},
    {"id": 4, "name": "Product4", "price": 4.5, "picture": "https://picsum.photos/200/300/?blur", "description": "Product's description 4"}
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