from django.contrib import admin

from moscow_events.apps.spots.models import PlaceType, Spot

admin.site.register(PlaceType)
admin.site.register(Spot)
