from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place, Image
from django.templatetags.static import static
import json

def index_page(request):
	
	places = Place.objects.all()
	
	list_of_json = []
	
	for place in places:
		lon, lat = place.longitude, place.latitude
		coordinates_to_dict = [float(lon), float(lat)]
		place_as_dict = {
		  "type": "Feature",
		  "geometry": {
			"type": "Point",
			"coordinates": coordinates_to_dict
		  },
		  "properties": {
			"title": place.title,
			"placeId": place.id,
			"detailsUrl": f"places/{place.id}/"
		  }
		}
		list_of_json.append(place_as_dict)
	
	data = {}
	to_template = { 'data': 
		{
		  "type": "FeatureCollection",
		  "features": list_of_json
		}
	}

	
	return render(request, 'index.html', to_template)

