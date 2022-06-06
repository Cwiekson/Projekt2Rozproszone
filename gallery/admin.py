from django.contrib import admin

# Register your models here.


from django.contrib.admin import register

from gallery.models import Photo


@register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'date',
        'title',
    ]
