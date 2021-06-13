from django.db import models


class PlaceType(models.Model):
    place_type_name = models.CharField(max_length=40)
    place_type_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.place_type_name}'


class Spot(models.Model):
    spot_name = models.CharField(max_length=40)
    address = models.CharField(max_length=300, default='', null=True)
    place_type = models.ForeignKey(PlaceType, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.spot_name}'
