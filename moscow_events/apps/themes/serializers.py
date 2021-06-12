from rest_framework import serializers

from moscow_events.apps.themes.models import Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('theme_name', )
