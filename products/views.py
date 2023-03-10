from django.shortcuts import render
from .models import Product, Category
from django.views.generic import ListView, DetailView, UpdateView, \
    CreateView, DeleteView

# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = '../templates/products/products.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = '../templates/products/product_detail.html'
    context_object_name = 'productdetails'


class CategoryList(ListView):
    model = Category
    template_name = '../templates/products/products.html'
    context_object_name = 'categories'


class CategoryDetails(DetailView):
    model = Category
    template_name = '../templates/products/product_category.html'
    context_object_name = 'categorydetails'