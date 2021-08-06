from django.shortcuts import render
from places.models import Place


def index_page(request):

    places = Place.objects.all()

    points_on_map = []

    for place in places:
        lon, lat = place.longitude, place.latitude
        coordinates = [lon, lat]
        place_serialized = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": coordinates
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f"places/{place.id}/"
            }
        }
        points_on_map.append(place_serialized)

    context = {'data':
        {
            "type": "FeatureCollection",
            "features": data
        }
    }
    return render(request, 'index.html', context)
