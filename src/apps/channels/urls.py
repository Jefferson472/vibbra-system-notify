from django.urls import path

from .views import AppView, ChannelListView


urlpatterns = [
    path('app/create/', AppView.as_view(), name='create_app'),
    path('channels/<int:app_id>/', ChannelListView.as_view(), name='channels_list'),
]
