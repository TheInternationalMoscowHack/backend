from rest_framework import serializers

from moscow_events.app.models import Event, Sphere, Spot, Theme


class SphereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sphere
        fields = ('sphere_name', )


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('theme_name', )


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('name', 'address', 'place_type')


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
    spheres_names = SphereSerializer(read_only=True, many=True)
    themes_names = ThemeSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = ('title', 'description', 'image', 'spot_name', 'address', 'is_free', 'date_from', 'date_to',
                  'restriction', 'district_name', 'spheres_names', 'themes_names')
