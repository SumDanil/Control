from django.db import models


class Comments(models.Model):
    full_name = models.CharField(max_length=254, blank=True, verbose_name='Полное имя пользователя')
    comment = models.TextField(max_length=500, blank=True, verbose_name='Коментарий')
    created_add = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Время добавления')
    rating = models.IntegerField(blank=True, verbose_name='Рейтинг')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=False, verbose_name='Фото')
    name_product = models.CharField(max_length=254, blank=False, verbose_name='Наименование товара')
    description_product = models.TextField(max_length=500, blank=False, verbose_name='Описание товара')

    def __str__(self):
        return self.name_product
