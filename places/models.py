from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = HTMLField(blank=True, verbose_name='Короткое описание')
    description_long = HTMLField(blank=True, verbose_name='Описание')
    latitude = models.FloatField(max_length=25, blank=True, verbose_name='Широта')
    longitude = models.FloatField(max_length=25, blank=True, verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

class Image(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    number = models.PositiveIntegerField(default=0, blank=True, verbose_name='Порядковый номер')
    place = models.ForeignKey(Place, related_name="images", on_delete=models.CASCADE, blank=True, verbose_name='Место')

    def __str__(self):
        return f'{self.number}, {self.place.title}'

    class Meta:
        ordering = ('number',)
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
