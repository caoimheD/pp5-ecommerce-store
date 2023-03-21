from django.shortcuts import render
from .models import Order, OrderLineItem
from django.views.generic import ListView, DetailView, UpdateView, \
    CreateView, DeleteView

# Create your views here.


#class Order(ListView):
#    model = Order
#    template_name = '../templates/checkout/checkout.html'
#    context_object_name = 'checkout'

#    cart = request.session.get('cart', {})
#    if not cart:
#        messages.error(request, "There's nothing in your bag at the moment")


class CreateOrder(CreateView):
    model = Order
    fields = 'full_name', 'email', 'phone_number', 'street_address1', \
             'street_address2', 'town_or_city', 'postcode', 'county', \
             'country'
    template_name = '../templates/checkout/checkout.html'
    context_object_name = 'checkout'