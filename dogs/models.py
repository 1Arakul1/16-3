from django.db import models
from django.conf import settings

class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название породы')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Кличка')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Порода')
    image = models.ImageField(upload_to='dogs/', blank=True, null=True, verbose_name='Изображение')
    age = models.IntegerField(verbose_name='Возраст')
    description = models.TextField(blank=True, verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'