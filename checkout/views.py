from django.shortcuts import render
from .models import Order, OrderLineItem
from django.views.generic import ListView, DetailView, UpdateView, \
    CreateView, DeleteView
from django.views import View
from .forms import OrderForm
from cart.context_processors import cart_contents

import stripe
import json

from django.conf import settings 
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt 


#class Order(ListView):
#    model = Order
#    template_name = '../templates/checkout/checkout.html'
#    context_object_name = 'checkout'

#    cart = request.session.get('cart', {})
#    if not cart:
#        messages.error(request, "There's nothing in your bag at the moment")


#class CreateOrder(CreateView):
#    model = Order
#    fields = 'full_name', 'email', 'phone_number', 'street_address1', \
#             'street_address2', 'town_or_city', 'postcode', 'county', \
#             'country'
#    template_name = '../templates/checkout/checkout.html'
#    context_object_name = 'checkout'

#    def cart(self, request):
#        cart = request.session.get('cart', {})
#        return cart

#    stripe_public_key = settings.STRIPE_PUBLIC_KEY
#    stripe_secret_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
   
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)



# From Stripe documentation


class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.data)
        # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=calculate_order_amount(data['items']),
                currency='eur',
                automatic_payment_methods={
                 'enabled': True,
                },
            )
            return jsonify({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return jsonify(error=str(e)), 403