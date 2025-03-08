from shop.models import *


def categories_processor(request):
    categories = ProductCategory.objects.all()
    context = {
        "categories": categories
    }

    return context



def products_processor(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return context