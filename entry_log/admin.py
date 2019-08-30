from django.contrib import admin
from entry_log.models import EntryLog

@admin.register(EntryLog)
class EntryLogAdmin(admin.ModelAdmin):
    list_display = ['car_id', 'entry_time']