from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Product, Category, Review
from django.views.generic import ListView, DetailView, UpdateView, \
    CreateView, DeleteView

# To view products and product details


class ProductList(ListView):
    model = Product
    template_name = '../templates/products/products.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = '../templates/products/product_detail.html'
    context_object_name = 'productdetails'

# To view categories


class CategoryList(ListView):
    model = Category
    template_name = '../templates/products/products.html'
    context_object_name = 'categories'


class CategoryDetails(DetailView):
    model = Category
    template_name = '../templates/products/product_category.html'
    context_object_name = 'categorydetails'

# Admin CRUD functionality


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    class that can be used in CRUD views to limit them to superuser only
    """

    def test_func(self):
        return self.request.user.is_superuser


class ProductCreate(SuperUserRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = '../templates/products/create_product.html'
    context_object_name = 'createproducts'

    def get_success_url(self):
        return reverse_lazy('products')
    
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs)


class ProductUpdate(SuperUserRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name = '../templates/products/update_product.html'
    context_object_name = 'updateproducts'

    def get_success_url(self):
        return reverse_lazy('productdetail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Product updated successfully!')
        return super(ProductUpdate, self).form_valid(form)


class ProductDelete(SuperUserRequiredMixin, DeleteView):
    model = Product
    template_name = '../templates/products/delete_product.html'
    context_object_name = 'deleteproducts'

    def get_success_url(self):
        return reverse_lazy('products')

    def form_valid(self, form):
        messages.success(self.request, 'Product deleted successfully!')
        return super(ProductDelete, self).form_valid(form)


# Reviews

class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    fields = 'name', 'rating', 'title', 'review'
    template_name = '../templates/products/create_review.html'
    context_object_name = 'createreview'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.productname = Product.objects.get(pk=self.kwargs['pk'])
        messages.success(self.request, 'You have left a review!')
        return super(CreateReview, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('productdetail', kwargs={'pk': self.kwargs['pk']})


class DeleteReview(SuperUserRequiredMixin, DeleteView):
    """
    For admin users to delete reviews
    """
    model = Review
    template_name = '../templates/products/delete_review.html'

    def form_valid(self, form):
        messages.success(self.request, 'Review deleted')
        return super(DeleteReview, self).form_valid(form)

    def get_success_url(self):
        self.product_pk = self.get_object().productname.pk
        return reverse_lazy('productdetail', kwargs={'pk': self.product_pk})