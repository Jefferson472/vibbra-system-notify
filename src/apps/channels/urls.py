from django.urls import path

from .views import AppView, ChannelDeleteView, ChannelListView


urlpatterns = [
    path('app/create/', AppView.as_view(), name='app_create'),
    path('channels/<int:app_id>/', ChannelListView.as_view(), name='channels_list'),
    path('channel/<int:pk>/delete/', ChannelDeleteView.as_view(), name='channel_delete'),
]
