from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from places.models import Place, Image

# Create your views here.
def id_api(request, post_id):
	place = get_object_or_404(Place.objects.filter(id = post_id))
	images = Image.objects.filter(places__in = Place.objects.filter(id = post_id))
	
	imgs = []
	for image in images:
		img_path = image.image.url
		imgs.append(img_path)
		
	respose_data = {
	'title': place.title,
	'imgs': imgs,
	'description_short': place.description_short,
	'description_long': place.description_long,
	'coordinates': "#"
	}
	return JsonResponse(respose_data, json_dumps_params={'ensure_ascii': False})