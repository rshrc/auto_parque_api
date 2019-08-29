from django.contrib import admin

from zone.models import Zone, Index, Slot

admin.site.site_header = 'Parque Space'


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ['number']


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ['zone', 'index', 'empty']
