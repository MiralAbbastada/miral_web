from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('console/', views.dashboard, name="dashboard"),
    path('add/', views.add_website, name="add_website"),
    path('delete/<int:pk>', views.delete_website, name="delete_website"),
]
