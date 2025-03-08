from django.urls import path

from shop.views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('about/', about_view, name='about_url'),
    path('contact/', contact_view, name='contact_url'),
    path('shop/', shop_view, name='shop_url'),
    path('product_details/<str:product_SKU>/', product_details, name='product_details_url'),
    path('product_by_category/<str:category_slug>/', products_by_category, name='products_by_category_url'),
    path('search/', search_view, name='search_url'),
]