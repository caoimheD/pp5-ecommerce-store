from django.urls import path
from . import views
from .views import profile, CreateContact

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('createcontact', CreateContact.as_view(), name='contact'),
]