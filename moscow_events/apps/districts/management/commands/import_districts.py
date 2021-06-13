import json

from django.core.management import BaseCommand

from moscow_events.apps.districts.models import District


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('D:\python_projects\data\district.json', 'r', encoding='utf-8') as file:
            districts = json.load(file)
            for district in districts.items():
                District.objects.create(district_name=district[1], district_id=district[0])
        return
