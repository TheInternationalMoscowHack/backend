from rest_framework.generics import ListAPIView

from moscow_events.app.models import Event
from moscow_events.app.serializers import EventListSerializer, EventRetrieveSerializer


class EventListView(ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()


class EventView(ListAPIView):
    serializer_class = EventRetrieveSerializer
    queryset = Event.objects.all()
