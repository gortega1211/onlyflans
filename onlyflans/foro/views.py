from django.shortcuts import render

def foro_home(request):
    return render(request, "foro/foro_page.html", {})