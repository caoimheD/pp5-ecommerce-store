from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, \
    CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile, contact
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

# Contact

class CreateContact(LoginRequiredMixin, CreateView):
    model = contact
    fields = 'email', 'review', 'message'
    template_name = '../templates/profiles/contact.html'
    context_object_name = 'contacthere'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['userreview'] = user.review_set.all
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.review = user.review_set.all
        messages.success(self.request, 'Request sent!')
        return super(CreateContact, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile')
