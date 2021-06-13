from django.urls import path

from moscow_events.apps.events.views import EventListView, EventView, FirstRecommendationView, \
    CollectionRecommendationsView, FinalRecommendationsView

urlpatterns = [
    path('events/', EventListView.as_view(), name='list_of_events'),
    path('events/<pk>/', EventView.as_view(), name='get_one_event'),
    path('first_recommendation/', FirstRecommendationView.as_view(), name='first_recommendation'),
    path('collection_recommendation/', CollectionRecommendationsView.as_view(), name='collection_recommendation'),
    path('recommendation_final/', FinalRecommendationsView.as_view(), name='recommendation_final'),
]
