from django.contrib import admin

from zone.models import Zone, Index, Slot, CarSlot

admin.site.site_header = 'Parque Space'


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ['zone_name', 'index_number', 'empty']


@admin.register(CarSlot)
class CarSlotAdmin(admin.ModelAdmin):
    list_display = ['id', 'slot_name', 'car_count']