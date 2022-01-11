from django.contrib import admin

from .models import Collection, Taille, Pointure, Couleur

@admin.register(Collection)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['id', 'annee']


@admin.register(Taille)
class TailleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Pointure)
class PointureAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Couleur)
class CouleurAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'hex_value']
