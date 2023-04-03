from django.contrib import admin
from django.urls import path
from . import views
from checkout.views import checkout, checkout_success, cache_checkout_data
from .webhooks import webhook

urlpatterns = [
    #path('', CreateOrder.as_view(), name='checkout'),
    path('', views.checkout, name='checkout'),
    #path('create-checkout-session/', views.create_checkout_session),
    #path('create-payment-intent/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data')
]