from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.index,name='home'),
    path('projects', views.projects,name='projects'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact')
    ]
