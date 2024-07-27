from django.urls import path

from .views import AppView, AppDeleteView, ChannelDeleteView, ChannelListView


urlpatterns = [
    path('app/create/', AppView.as_view(), name='app_create'),
    path('app/delete/<int:pk>', AppDeleteView.as_view(), name='app_delete'),
    path('channels/<int:app_id>/', ChannelListView.as_view(), name='channels_list'),
    path('channel/delete/<int:pk>/', ChannelDeleteView.as_view(), name='channel_delete'),
]
