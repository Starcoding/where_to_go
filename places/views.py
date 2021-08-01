from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from places.models import Place, Image


def id_api(request, post_id):
    place = get_object_or_404(Place, id=post_id)
    images = place.images.all()
    imgs_urls = []
    for image in images:
        imgs_urls.append(image.image.url)

    respose_data = {
        'title': place.title,
        'imgs': imgs_urls,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': f"{place.latitude}, {place.longitude}"
    }
    return JsonResponse(respose_data, json_dumps_params={'ensure_ascii': False})
