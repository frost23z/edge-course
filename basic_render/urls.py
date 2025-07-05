from django.urls import path

from . import views

app_name = 'basic_render'

urlpatterns = [
    path('http/', views.http, name='http'),
    path('template/', views.template, name='template'),
]
