from django.shortcuts import render
from places.models import Place


def index_page(request):

    places = Place.objects.all()

    data = []

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
        data.append(place_serialized)

    points_on_map = {'data':
        {
            "type": "FeatureCollection",
            "features": data
        }
    }
    return render(request, 'index.html', points_on_map)
