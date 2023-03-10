from django.contrib import admin
from django.urls import path
from . import views
from products.views import ProductList, ProductDetail, CategoryList, CategoryDetails


urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<int:pk>/', ProductDetail.as_view(), name='productdetail'),
    path('', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetails.as_view(), name='categorydetails'),
]