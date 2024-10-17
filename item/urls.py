#!/usr/bin/python3

from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
        path('new/', view.new, name='new'),
        path('<int:pk>/', views.detail, name='detail'),
        ]
