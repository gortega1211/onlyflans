from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .models import Flan, ContactForm
from .forms import ContactFormForm

def index(request):
    flans = Flan.objects.all()
    return render(request, "index.html", {"flans": flans})

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())

def welcome(request):
    template = loader.get_template("welcome.html")
    return HttpResponse(template.render())

def contact(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/success")
    else:
        form = ContactFormForm
    return render(request, "contact.html", {"form": form})

def success(request):
    print(request)
    return render(request, "success.html", {})