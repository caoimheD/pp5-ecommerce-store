from django.contrib import admin
from django.urls import path
from . import views
from checkout.views import StripeIntentView, checkout

urlpatterns = [
    #path('', CreateOrder.as_view(), name='checkout'),
    path('', views.checkout, name='checkout'),
    #path('create-checkout-session/', views.create_checkout_session),
    path('create-payment-intent/', StripeIntentView.as_view(), name='create-payment-intent'),
]