from django.contrib import admin
from django.urls import path
from . import views
from products.views import ProductList, ProductDetail

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<int:pk>/', ProductDetail.as_view(), name='productdetail'),
]