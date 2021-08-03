from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin

# Register your models here.


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ("image_preview",)


    def image_preview(self, obj):
        url = obj.image.url
        return format_html('<img src="{}" height="100" width="200" />', url)

class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)
    autocomplete_fields = ['place']


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    search_fields = ['title']

admin.site.register(Image, ImageAdmin)
admin.site.register(Place, PlaceAdmin)
