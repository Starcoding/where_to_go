from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image
import requests
import json
from PIL import Image as PIL_Image
from io import BytesIO
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Adding a new place from url'
    
    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+')
        
    def handle(selsf, *args, **options):
        for url in options['urls']:
            # try:                
            place_raw = requests.get(url).json()
            place, created = Place.objects.get_or_create(
                title = place_raw["title"],
                description_short = place_raw["description_short"],
                description_long = place_raw["description_long"],
                latitude = place_raw["coordinates"]["lat"],
                longitude = place_raw["coordinates"]["lng"],
            )
            img_number = 1
            for img_url in place_raw["imgs"]:
                request = requests.get(img_url)
                img_name = img_url.split("/")[len(img_url.split("/"))-1]
                img = Image.objects.get_or_create(places=place, number=img_number)
                img_number = img_number + 1
                f = ContentFile(request.content)
                img[0].image.save(img_name, f, save=True) 

                

            
            