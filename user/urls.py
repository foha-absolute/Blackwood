from django.urls import path
from user.views import *

urlpatterns = [
    path('cart/', cart_view, name='cart_url'),
    path('cart/<str:product_SKU>/', add_cart_view, name='add_cart_url'),
    path('cart/<str:product_SKU>/remove/', remove_cart_view, name='remove_cart_url'),
    path('sign-in/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    path('registration/', registration_view, name='registration_url'),
    path('wishlist/<str:product_SKU>/', add_wishlist_view, name='add_wishlist_url'),
    path('choose/', choose_view, name='choose_url'),
    path('wishlist/', wishlist_view, name='wishlist_url')
]