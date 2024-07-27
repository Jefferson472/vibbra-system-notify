from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import ListView

from apps.channels.models.channel import Channel


class ChannelListView(LoginRequiredMixin, ListView):
    model = Channel

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset.filter(app__id=self.kwargs.get("app_id"))
