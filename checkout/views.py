from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Order, OrderLineItem
from django.views.generic import ListView, DetailView, UpdateView, \
    CreateView, DeleteView
from django.views import View
from .forms import OrderForm
from products.models import Product
from cart.context_processors import cart_contents
from django.contrib import messages
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

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()

            for item_id, item_data in cart.items():
                product = Product.objects.get(id=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
      
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
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

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


# From Stripe documentation
"""
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
"""