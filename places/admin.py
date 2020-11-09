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
        return format_html(f'<img src="{url}" max-height="200px" width="200px" />')


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Image)
admin.site.register(Place, PlaceAdmin)
