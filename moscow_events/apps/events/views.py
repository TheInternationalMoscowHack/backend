from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from moscow_events.apps.events.models import Event
from moscow_events.apps.events.serializers import EventListSerializer, EventRetrieveSerializer
from moscow_events.settings import GLOBAL_RECOMMENDATION_DICT


class EventListView(ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['spheres', 'themes', 'restriction', 'is_free']


class EventView(ListAPIView):
    serializer_class = EventRetrieveSerializer
    queryset = Event.objects.all()


class FirstRecommendationView(APIView):

    def post(self, request):
        """
        Keeps recommendations in a global var where the key is UID after the first three questions
        The value by the dict key is updated after next using
        """
        uid = request.GET.get('uid')
        district = request.POST['district']
        date = request.POST['date']
        restriction = request.POST['restriction']
        date_format = datetime.strptime(date, '%Y-%m-%d')
        events = Event.objects.filter(district__district_name=district, date_from__lte=date_format,
                                      date_to__gte=date_format, restriction=restriction)
        GLOBAL_RECOMMENDATION_DICT[uid] = events
        return Response(status=status.HTTP_200_OK)


class CollectionRecommendationsView(APIView):

    def post(self, request):
        """
        Collections recommendations in a global var where the key is UID after each question
        """
        uid = request.GET.get('uid')
        return Response(status=status.HTTP_200_OK)
