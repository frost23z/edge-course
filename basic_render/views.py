from django.http import HttpResponse
from django.shortcuts import render


def http(request):
    return HttpResponse("Hello World! This is a basic HTTP response.")


def template(request):
    return render(request, 'index.html', {
        'title': 'Simple HTML Rendering',
        'message': 'This is a simple HTML page rendered with Django templates.'
    })
