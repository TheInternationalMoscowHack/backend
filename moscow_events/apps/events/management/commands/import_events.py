import json

from django.core.management import BaseCommand

from moscow_events.apps.districts.models import District
from moscow_events.apps.events.models import Event
from moscow_events.apps.spheres.models import Sphere
from moscow_events.apps.spots.models import Spot


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('D:\python_projects\data\events.json', 'r', encoding='utf-8') as file:
            events = json.load(file)
            for event in events:
                if not event['districts']:
                    new_event = Event.objects.create(
                        title=event['title'],
                        description=event['text'],
                        image='https://www.mos.ru' + event['image']['original']['src'],
                        is_free=event['free'],
                        date_from=event['date_from'],
                        date_to=event['date_to'],
                        restriction=event['restriction']['age'],
                        spot=Spot.objects.filter(spot_name=event['spots'][0]['title']).first(),
                    )
                else:
                    new_event = Event.objects.create(
                        title=event['title'],
                        description=event['text'],
                        image='https://www.mos.ru' + event['image']['original']['src'],
                        is_free=event['free'],
                        date_from=event['date_from'],
                        date_to=event['date_to'],
                        restriction=event['restriction']['age'],
                        district=District.objects.filter(district_id=event['districts'][0]['id']).first(),
                        spot=Spot.objects.filter(spot_name=event['spots'][0]['title']).first(),
                    )
                for sphere in event['spheres']:
                    new_event.spheres.add(Sphere.objects.filter(sphere_name=sphere['title']).first())
        return
