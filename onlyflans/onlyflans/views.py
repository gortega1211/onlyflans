from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request) -> HttpResponse:
    return HttpResponse("Hello World!")

def bye_world(request) -> HttpResponse:
    return HttpResponse("Bye World!")

def hi(request):
    return render(request, "hi.html", {})

def dynamic_content(request):
    categories = ["Python", "Django", "HTML", "CSS", "JavaScript"]
    context = {"categories": categories}
    return render(request, 'dynamicContent.html', context)

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})