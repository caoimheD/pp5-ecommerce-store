from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, \
    CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def cart(request):
    """ Displays cart page """

    return render(request, 'cart/cart.html')


@login_required
def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


@login_required
def edit_cart(request, item_id):
    """Adjust the quantity of an item"""

    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect('cart')


@login_required
def remove_from_cart(request, item_id):
    """Delete an item from the cart"""

    cart = request.session.get('cart', {})
    cartitems = list(cart.keys())

    if item_id in cartitems:
        cart.pop(item_id, None)
  
    request.session['cart'] = cart
    return redirect('cart')
