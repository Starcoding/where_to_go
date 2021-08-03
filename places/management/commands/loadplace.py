from django.core.management.base import BaseCommand
from places.models import Place, Image
import requests
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
            for img_number, img_url in enumerate(place_raw["imgs"], 1):
                request = requests.get(img_url)
                img_name = img_url.split("/")[len(img_url.split("/"))-1]
                img = Image.objects.get_or_create(places=place, number=img_number)
                f = ContentFile(request.content)
                img[0].image.save(img_name, f, save=True) 

                

            
            