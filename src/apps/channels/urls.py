from django.urls import path

from .views import (
    AppDeleteView,
    AppView,
    ChannelCreateView,
    ChannelDeleteView,
    ChannelListView,
)


urlpatterns = [
    path('app/create/', AppView.as_view(), name='app_create'),
    path('app/delete/<int:pk>', AppDeleteView.as_view(), name='app_delete'),
    path('app/<int:app_id>/channels/', ChannelListView.as_view(), name='channels_list'),
    path('app/<int:app_id>/channel/create/<str:type>/', ChannelCreateView.as_view(),
         name='channel_create'),
    path('channel/delete/<int:pk>/', ChannelDeleteView.as_view(),
         name='channel_delete'),
]
