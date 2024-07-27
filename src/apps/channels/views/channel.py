from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView

from apps.channels.models.channel import Channel
from apps.channels.models.app import App


class ChannelListView(LoginRequiredMixin, ListView):
    model = Channel

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset.filter(app__id=self.kwargs.get("app_id"))


class ChannelDeleteView(LoginRequiredMixin, DeleteView):
    model = Channel

    def get_success_url(self) -> str:
        channel = self.object
        return reverse_lazy('channels_list', kwargs={"app_id": channel.app_id})
