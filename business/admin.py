from django.contrib import admin
from .models import Business, Media
from django.utils.html import format_html

from solo.admin import SingletonModelAdmin






@admin.register(Business)
class BusinesAdmin(SingletonModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    # def has_add_permission(self, request):
    #     return False


@admin.register(Media)
class BusinesAdmin(admin.ModelAdmin):
    def image_tag(self):
        return format_html('<img src="{}" height="150"  />'.format(self.big_slide.url))
    list_display = ('id', 'big_slide', 'order', 'actif', 'is_big', 'is_small', 'page', image_tag)
    list_editable = ['big_slide', 'order', 'actif', 'is_big', 'is_small', 'page']

    list_display_links = ('id',)

    # def has_add_permission(self, request):
    #     return False
