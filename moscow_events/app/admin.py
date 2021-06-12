from django.contrib import admin

from moscow_events.app.models import District, Sphere, Theme, PlaceType, Event

admin.site.register(District)
admin.site.register(Sphere)
admin.site.register(Theme)
admin.site.register(PlaceType)
admin.site.register(Event)
