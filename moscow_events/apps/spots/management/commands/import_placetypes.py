import json

from django.core.management import BaseCommand

from moscow_events.apps.spots.models import PlaceType


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('D:\python_projects\data\places.json', 'r', encoding='utf-8') as file:
            place_types = json.load(file)
            for place_type in place_types['items']:
                PlaceType.objects.create(place_type_name=place_type['title'], place_type_id=place_type['id'])
        return
