from django.contrib import admin
from shop.models import *
from mptt.admin import DraggableMPTTAdmin
# Register your models here.





class ProductAdditionalInfoTabularInline(admin.TabularInline):
    model = ProductAdditionalInfo
    fk_name = 'product'
    extra = 5

class ProductImageTabularInline(admin.TabularInline):
    model = ProductImage
    fk_name = 'product'
    extra = 5

@admin.register(ProductCategory)
class ProductCategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'id', 'title', 'parent')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'SKU', 'price', 'category', 'brand')
    list_display_links = ('title',)
    inlines = [ProductAdditionalInfoTabularInline, ProductImageTabularInline]


admin.site.register(ProductReview)
