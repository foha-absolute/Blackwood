from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User
# Create your models here.



class ProductCategory(MPTTModel):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255,
                            unique=True)
    image = models.ImageField(upload_to='shop/categories/', null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'


class ProductBrand(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product Brand'
        verbose_name_plural = 'Product Brands'


class Product(models.Model):
    thumbnail = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=255, unique=True)
    short_desc = models.TextField()
    desc = CKEditor5Field()
    SKU = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    discount = models.PositiveIntegerField()
    brand = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name='products')


    def get_discount_price(self):
        percentage = 100 - self.discount

        return (self.price / 100) * percentage

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductMainCharacteristics(models.Model):
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_characteristics')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'ProductMainCharacteristic'
        verbose_name_plural = 'ProductMainCharacteristics'


class ProductAdditionalInfo(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    product = models.ForeignKey(Product, related_name='product_additional_information', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} | {self.value} | {self.product}'



class ProductReview(models.Model):
    review = models.TextField()
    author = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, related_name='product_reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f'Review by {self.author.username} for {self.product.title}'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_photos')

    def __str__(self):
        return f'{self.id} | {self.product}'
