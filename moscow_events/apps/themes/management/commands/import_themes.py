import json

from django.core.management import BaseCommand

from moscow_events.apps.themes.models import Theme


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('D:\python_projects\data\\themes.json', 'r', encoding='utf-8') as file:
            themes = json.load(file)
            for theme in themes:
                Theme.objects.create(theme_name=theme['title'])
        return
