from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = "inventory"
# Includes the basic url patterns not closely related to our database
urlpatterns = [
    path("<int:pk>", views.get_one_inventory, name="inventory"),
    path("", views.inventorylist, name="inventorylist"),
    path("create", views.inventory_create, name="create"),
    path("delete/<int:pk>", views.inventory_delete, name="delete"),
    path("edit/<int:pk>", views.inventory_edit, name="edit"),
    path("download", views.csv_create, name="download"),
]
