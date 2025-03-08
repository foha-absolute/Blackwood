from django.shortcuts import render, get_object_or_404, redirect
from shop.models import *
from shop.forms import *
from user.models import *
# Create your views here.

def index_view(requests):
    context = {
        'title': 'Главная страница'
    }

    return render(requests, 'shop/index.html', context)

def about_view(requests):
    context = {
        'title': 'О нас'
    }

    return render(requests, 'shop/about.html', context)


def contact_view(requests):
    context = {
        'title': 'Связаться с нами'
    }

    return render(requests, 'shop/contact.html', context)


def shop_view(requests):
    context = {
        'title': 'Магазин'
    }

    return render(requests, 'shop/shop.html', context)


def product_details(request, product_SKU):
    product = Product.objects.get(SKU=product_SKU)
    additionalInfo = ProductAdditionalInfo.objects.filter(product=product)
    reviews = ProductReview.objects.filter(product=product)  # Красное это переменная класса мы проверяем совпадает ли переменная класса с текущей переменной
    images = ProductImage.objects.filter(product=product)
    favorites = Favorite.objects.filter(user=request.user)
    favorites = [i.product for i in favorites]  # list comprehension ( генератор)
    if request.method == "POST":
        form = ReviewForm(data=request.POST)

        if form.is_valid():
            review = form.save(commit=False) # не записывать в базу сразу
            review.author = request.user
            review.product = product
            review.save()

            return redirect('product_details_url', product_SKU)
        else:
            return redirect('product_details_url', product_SKU)
    else:
        form = ReviewForm()



    context = {
        'title': f'О продукте {product.title}',
        'product': product,
        'additionalInfo': additionalInfo,
        'reviews': reviews,
        'images': images,
        'form': form,
        'favorites': favorites
    }

    return render(request, 'shop/product-details.html', context)


def products_by_category(request, category_slug):
    category = get_object_or_404(ProductCategory, slug=category_slug)
    products = Product.objects.filter(category=category)  ## Это как WHERE в SQL


    context = {
        'products': products,
        'category': category
    }

    return render(request, 'shop/shop.html', context)

def search_view(request):
    query = request.GET.get('q')

    products = Product.objects.filter(
        title__icontains=query  # Это значит если титул продукта совпадает с запросом
    )

    context = {
        'products': products,
        'title': 'Результаты поиска'
    }

    return render(request, 'shop/search.html', context)

