from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description_short = HTMLField()
    description_long = HTMLField()
#    coordinates = models.JSONField()
    latitude = models.CharField(max_length=25, blank=True)
    longitude = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(blank=False)
    number = models.PositiveIntegerField(default=0, blank=False, null=False)
    places = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number}, {self.places.title}'

    class Meta:
        ordering = ('number',)
