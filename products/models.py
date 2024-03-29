from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pages = models.IntegerField(default=1, null=True, blank=True)
    year = models.IntegerField(default=1, null=True, blank=True)
    publisher = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    productname = models.ForeignKey('Product', null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False,
                            default=None)
    rating = models.IntegerField(default=1, null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False,
                             default=None)
    review = models.TextField()

    def __str__(self):
        return self.title