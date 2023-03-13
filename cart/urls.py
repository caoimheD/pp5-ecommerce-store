from django.contrib import admin
from django.urls import path
from . import views
from .views import CreateCart, add_to_cart

urlpatterns = [
    path('', views.cart, name='cart'),
    path('addcart/', CreateCart.as_view(),
         name='addcart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
]