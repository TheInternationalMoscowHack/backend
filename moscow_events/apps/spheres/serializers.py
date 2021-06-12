from rest_framework import serializers

from moscow_events.apps.spheres.models import Sphere


class SphereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sphere
        fields = ('sphere_name', )
