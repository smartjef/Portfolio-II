from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cv/', views.cv, name='cv'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('aboutme/', views.aboutme, name='about'),
]