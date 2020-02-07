from django.contrib import admin

from zone.models import Slot

admin.site.site_header = 'Parque Space'

@admin.register(Slot)
class CarSlotAdmin(admin.ModelAdmin):
    list_display = ['id', 'slot_name', 'car_count']