from django.contrib import admin
from django.urls import path
from . import views
from products.views import ProductList, ProductDetail, CategoryList, \
    CategoryDetails, ProductCreate, ProductUpdate, ProductDelete, \
    CreateReview


urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<int:pk>/', ProductDetail.as_view(), name='productdetail'),
    path('', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetails.as_view(), name='categorydetails'),
    path('new/', ProductCreate.as_view(), name='createproduct'),
    path('<int:pk>/delete/', ProductDelete.as_view(),
         name='deleteproduct'),
    path('<int:pk>/update/', ProductUpdate.as_view(),
         name='updateproduct'),
    path('<int:pk>/newreview/', CreateReview.as_view(), name='createreview'),
]