from django.contrib import admin
from django.urls import path
from . import views
from checkout.views import CreateOrder

urlpatterns = [
    path('', CreateOrder.as_view(), name='checkout'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
]