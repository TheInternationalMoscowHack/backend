from django.db import models

from moscow_events.apps.districts.models import District
from moscow_events.apps.spheres.models import Sphere
from moscow_events.apps.spots.models import Spot
from moscow_events.apps.themes.models import Theme
from moscow_events.settings import MEDIA_EVENT_IMAGE_DIR


class Event(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.CharField(max_length=500)
    is_free = models.BooleanField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    restriction = models.PositiveIntegerField(default=0)
    click_count = models.PositiveIntegerField(default=0)
    district = models.ForeignKey(District, on_delete=models.CASCADE, default='', null=True)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    spheres = models.ManyToManyField(Sphere)
    themes = models.ManyToManyField(Theme)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
