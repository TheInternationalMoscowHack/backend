from django.urls import path

from moscow_events.app.views import EventListView, EventView

urlpatterns = [
    path('events/', EventListView.as_view(), name='list_of_events'),
    path('events/<pk>/', EventView.as_view(), name='get_one_event'),
]