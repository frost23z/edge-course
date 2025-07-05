from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! This is a basic HTTP response.")

def html(request):
    return render(request, 'basic_render/index.html', {
        'title': 'Simple HTML Rendering',
        'message': 'This is a simple HTML page rendered with Django templates.'
    })