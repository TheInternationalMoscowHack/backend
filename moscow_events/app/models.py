from django.db import models

from moscow_events.settings import MEDIA_EVENT_IMAGE_DIR


class District(models.Model):

    district_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.district_name}'


class Sphere(models.Model):
    sphere_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.sphere_name}'


class Theme(models.Model):
    theme_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.theme_name}'


class PlaceType(models.Model):
    place_type_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.place_type_name}'


class Spot(models.Model):
    spot_name = models.CharField(max_length=40)
    address = models.CharField(max_length=300)
    place_type = models.ForeignKey(PlaceType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.spot_name}'


class Event(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to=MEDIA_EVENT_IMAGE_DIR)
    is_free = models.BooleanField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    restriction = models.PositiveIntegerField(default=0)
    click_count = models.PositiveIntegerField(default=0)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    spheres = models.ManyToManyField(Sphere)
    themes = models.ManyToManyField(Theme)

    def __str__(self):
        return f'{self.title}'
