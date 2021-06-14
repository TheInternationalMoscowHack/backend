from datetime import datetime
import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from moscow_events.apps.events.models import Event
from moscow_events.apps.events.serializers import EventListSerializer, EventRetrieveSerializer
from moscow_events.settings import GLOBAL_RECOMMENDATION_DICT
from reccomendations.user_event import UserPerfectEvent


def get_json_from_queryset(queryset):
    events_list = []
    for event in queryset:
        event_dict = {
            'id': event.id,
            'title': event.title,
            'text': event.description,
            'spheres': [sphere.sphere_name for sphere in event.spheres.all()]
        }
        events_list.append(event_dict)
    return json.dumps(events_list)


class EventListView(ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.filter(date_to__gte=datetime.now()).filter(date_from__lte=datetime.now())
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['spheres', 'themes', 'restriction', 'is_free']


class EventView(ListAPIView):
    serializer_class = EventRetrieveSerializer
    queryset = Event.objects.all()


class FirstRecommendationView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        """
        Храним рекомендации после первых трех вопросов пользователю в глобальной переменной в виде словаря,
        ключем выступает UID,
        при повторном обращении к вопросам значение по UID обнволяется
        """
        uid = request.GET.get('uid')
        print(request.data)
        district = request.data['district']
        date = request.data['date']
        categories = request.data['categories']
        # categories = categories[2:-2].split("', '")
        date_format = datetime.strptime(date, '%Y-%m-%d')
        events = Event.objects.filter(district__district_name=district).filter(date_from__lte=date_format).filter(
            date_to__gte=date_format)
        list_events = [event.id for event in events]
        events_json = get_json_from_queryset(events)
        user = UserPerfectEvent(events_json)
        user.set_answer(categories)
        GLOBAL_RECOMMENDATION_DICT[uid] = [list_events, user]
        return Response(status=status.HTTP_200_OK)


class CollectionRecommendationsView(APIView):

    def post(self, request):
        """
        Получаем ответ на вопрос от пользователя,
        обновляем рекомендации в глобальной переменной после аналитики от DataScience
        """
        uid = request.GET.get('uid')
        user = GLOBAL_RECOMMENDATION_DICT[uid][1]
        response_data = request.POST
        user.set_answer(response_data)
        recommendations = user.get_events()
        GLOBAL_RECOMMENDATION_DICT[uid][0] = recommendations
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        """
        Отправляем следующий вопрос пользователю
        """
        uid = request.GET.get('uid')
        user = GLOBAL_RECOMMENDATION_DICT[uid][1]
        json_question = user.get_questions()
        return Response(json_question, status=status.HTTP_200_OK)


class FinalRecommendationsView(APIView):

    def get(self, request):
        uid = request.GET.get('uid')
        user = GLOBAL_RECOMMENDATION_DICT[uid][1]
        recommendations = user.get_events()
        queryset = Event.objects.filter(pk__in=recommendations)
        serializer = EventListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
