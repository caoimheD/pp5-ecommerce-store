from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Product, Category
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


class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    template_name = '../templates/products/create_product.html'
    context_object_name = 'createproducts'

    def get_success_url(self):
        return reverse_lazy('products')


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    template_name = '../templates/products/update_product.html'
    context_object_name = 'updateproducts'

    def get_success_url(self):
        return reverse_lazy('productdetail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Product updated successfully!')
        return super(ProductUpdate, self).form_valid(form)


class ProductDelete(DeleteView):
    model = Product
    template_name = '../templates/products/delete_product.html'
    context_object_name = 'deleteproducts'

    def get_success_url(self):
        return reverse_lazy('products')

    def form_valid(self, form):
        messages.success(self.request, 'Product deleted successfully!')
        return super(ProductDelete(), self).form_valid(form)