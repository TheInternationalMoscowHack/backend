import json

from django.core.management import BaseCommand

from moscow_events.apps.spots.models import PlaceType, Spot


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('D:\python_projects\data\spots.json', 'r', encoding='utf-8') as file:
            spots = json.load(file)
            for spot in spots:
                Spot.objects.create(
                    spot_name=spot['title'],
                    address=spot['address'],
                    place_type=PlaceType.objects.filter(place_type_id=spot['place_type_id']).first()
                )
        return
