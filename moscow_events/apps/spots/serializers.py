from rest_framework import serializers

from moscow_events.apps.spots.models import Spot


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('name', 'address', 'place_type')
