import json

from django.core.management import BaseCommand

from moscow_events.apps.spheres.models import Sphere


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('D:\python_projects\data\spheres.json', 'r', encoding='utf-8') as file:
            spheres = json.load(file)
            for sphere in spheres:
                Sphere.objects.create(sphere_name=sphere['title'])
        return
