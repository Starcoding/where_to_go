from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from places.models import Place


def get_place_by_id(request, post_id):
    place = get_object_or_404(Place, id=post_id)
    images = place.images.all()
    imgs_urls = [image.image.url for image in images]

    respose = {
        'title': place.title,
        'imgs': imgs_urls,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }
    return JsonResponse(respose, json_dumps_params={'ensure_ascii': False})
