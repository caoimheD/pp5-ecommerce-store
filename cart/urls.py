from django.contrib import admin
from django.urls import path
from . import views
from .views import add_to_cart, edit_cart, remove_from_cart

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('edit/<item_id>/', views.edit_cart, name='edit_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
]