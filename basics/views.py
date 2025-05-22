from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world! This is the index view of the basics app.")


def html(request):
    return render(request, 'view.html')
