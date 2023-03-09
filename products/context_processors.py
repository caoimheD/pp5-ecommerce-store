from .models import Category, Product
from . import urls


def category_list(request):
    return {
        "categories": Category.objects.all()
    }