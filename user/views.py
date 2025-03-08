from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from user.forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shop.models import *
from user.models import *
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
@login_required
def cart_view(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart)
    context = {
        'title': 'Корзина',
        'cart': cart,
        'total_price': total_price
    }

    return render(request, 'user/cart.html', context)




def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.success(request, "Вы успешно вошли в аккаунт!")
                return redirect('index_url')
            else:
                return redirect('choose_url')
        else:
            messages.error(request, "Ошибка входа! Проверьте логин и пароль.")

    else:
        messages.error(request, "Ошибка входа! Проверьте логин и пароль.")

    context = {
        'sign_in': LoginForm(),
        'title': 'Вход'
    }

    return render(request, 'user/sign-in.html', context)

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта.")  # Уведомление о выходе
    return redirect('login_url')


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно! Теперь войдите в аккаунт!")
            return redirect('choose_url')
        else:
            messages.error(request, "Ошибка в заполнении формы!")
            return redirect('choose_url')

    context = {
        'sign_up': RegistrationForm(),
        'title': 'Регистрация'
    }

    return render(request, 'user/sign-up.html', context)




def choose_view(request):
    context = {
        'title': '?'
    }

    return render(request, 'user/choose.html', context)

@login_required
def add_wishlist_view(request, product_SKU):
    product = get_object_or_404(Product, SKU=product_SKU)
    wishlist, created = Favorite.objects.get_or_create(user=request.user, product=product)

    if not created:
        wishlist.delete()

    return redirect('wishlist_url')

@login_required
def wishlist_view(request):
    favorites = Favorite.objects.filter(user=request.user)
    context = {
        'title': 'Список желания',
        'favorites': favorites
    }

    return render(request, 'user/wishlist.html', context)

@login_required
def add_cart_view(request, product_SKU):
    quantity = int(request.POST.get('quantity', 1))
    product = get_object_or_404(Product, SKU=product_SKU)
    cart, created = Cart.objects.get_or_create(user=request.user, product=product, defaults={'quantity': quantity})
    if not created:
        cart.quantity += quantity
        cart.save()

    messages.success(request, f'{quantity} шт. "{product.title}" добавлено в корзину!')

    return redirect('cart_url')

@login_required
def remove_cart_view(request, product_SKU):
    product = Product.objects.get(SKU=product_SKU)
    cart = Cart.objects.filter(user=request.user, product=product)

    if cart:
        cart.delete()


    return redirect('cart_url')