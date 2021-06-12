from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from moscow_events.apps.events.models import Event
from moscow_events.apps.events.serializers import EventListSerializer, EventRetrieveSerializer


class EventListView(ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['spheres', 'themes', 'restriction', 'is_free']


class EventView(ListAPIView):
    serializer_class = EventRetrieveSerializer
    queryset = Event.objects.all()
