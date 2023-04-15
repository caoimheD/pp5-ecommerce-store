from django.contrib import admin
from .models import UserProfile, contact

admin.site.register(UserProfile)
admin.site.register(contact)