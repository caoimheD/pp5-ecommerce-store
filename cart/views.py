from django.shortcuts import render, redirect
from .models import Cart
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


class CartList(ListView):
    model = Cart
    template_name = '../templates/products/cart.html'
    context_object_name = 'cart'


class CartDetail(DetailView):
    model = Cart
    template_name = '../templates/products/cart.html'
    context_object_name = 'cartdetails'


class CreateCart(LoginRequiredMixin, CreateView):
    model = Cart
    fields = 'product',
    template_name = '../templates/cart/add_cart.html'
    context_object_name = 'addcart'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateCart, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('products')


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


def edit_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('bag', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    cartitems = list(cart.keys())

    if item_id in cartitems:
        cart.pop(item_id, None)
  
    request.session['cart'] = cart
    return redirect('cart')
