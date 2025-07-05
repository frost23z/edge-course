from django.urls import path
from . import views

app_name = 'basic_render'

urlpatterns = [
    path('http/', views.index, name='index'),
    path('html/', views.html, name='html'),
]