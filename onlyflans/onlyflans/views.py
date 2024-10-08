from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hola mundo")

def bye_world(request):
    return HttpResponse("Adios mundo")