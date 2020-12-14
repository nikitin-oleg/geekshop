from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(verbose_name='название', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True, verbose_name='картинка')
    short_desc = models.CharField(verbose_name='краткое описание', max_length=120, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Contacts(models.Model):
    city = models.CharField(verbose_name='город', max_length=64)
    phone = models.CharField(verbose_name='телефон', max_length=64)
    email = models.CharField(verbose_name='email', max_length=64)
    address = models.CharField(verbose_name='адрес', max_length=64)

    def __str__(self):
        return f"{self.city}"
