from django.contrib import admin
from .models import Venue, EventUser, Event

# Register your models here.
# admin.site.register(Venue)
admin.site.register(EventUser)
# admin.site.register(Event)
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address' )

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'attendees', 'eve_description', 'manager', 'man_phone','start_time','end_time')
    list_display = ('name', 'event_date', )
    list_filter = ('venue', 'event_date')
    ordering = ('event_date',)