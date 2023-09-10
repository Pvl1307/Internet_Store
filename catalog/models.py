from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name_of_category = models.CharField(max_length=100, verbose_name='Категория')
    description_of_category = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name_of_category} ({self.description_of_category[:20]}...)'

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name_of_product = models.CharField(max_length=100, verbose_name='Название')
    description_of_product = models.TextField(verbose_name='Описание', **NULLABLE)
    product_img = models.ImageField(upload_to='product/', verbose_name='Фото', **NULLABLE)
    category_of_product = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price_of_product = models.FloatField(verbose_name='Цена')
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    date_of_last_change = models.DateTimeField(verbose_name='Последнее изменение', **NULLABLE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')

    def __str__(self):
        return (f'{self.name_of_product}.'
                f'Категория: {self.category_of_product}. '
                f'Цена: {self.price_of_product}')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(max_length=50, verbose_name='Номер версии', **NULLABLE)
    version_name = models.CharField(max_length=50, verbose_name='Название версии')
    is_active = models.BooleanField(verbose_name='В наличии', default=False)

    def __str__(self):
        return f'{self.version_number}/{self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
