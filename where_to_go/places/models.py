from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = HTMLField(blank=True)
    description_long = HTMLField(blank=True)
    latitude = models.FloatField(max_length=25, blank=True)
    longitude = models.FloatField(max_length=25, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    number = models.PositiveIntegerField(default=0, blank=True)
    places = models.ForeignKey(Place, related_name="images", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.number}, {self.places.title}'

    class Meta:
        ordering = ('number',)
