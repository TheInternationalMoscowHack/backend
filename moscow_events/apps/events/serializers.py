from rest_framework import serializers

from moscow_events.apps.events.models import Event


class EventListSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='spot.address', read_only=True)
    spot_name = serializers.CharField(source='spot.spot_name', read_only=True)
    district_name = serializers.CharField(source='district.district_name', read_only=True)

    class Meta:
        model = Event
        fields = ('title', 'image', 'is_free', 'spot_name', 'address', 'date_from', 'date_to', 'restriction',
                  'district_name')


class EventRetrieveSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='spot.address', read_only=True)
    spot_name = serializers.CharField(source='spot.spot_name', read_only=True)
    district_name = serializers.CharField(source='district.district_name', read_only=True)

    class Meta:
        model = Event
        fields = ('title', 'description', 'image', 'spot_name', 'address', 'is_free', 'date_from', 'date_to',
                  'restriction', 'district_name', 'spheres', 'themes')
        depth = 1
