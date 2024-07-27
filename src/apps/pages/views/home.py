from typing import Any

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from apps.channels.models import Channel
from apps.channels.models.app import App


class HomePage(TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs) -> dict[str, Any]:
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('account_login'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        channels = Channel.objects.filter(
            app__user=self.request.user).select_related("app")
        channels_apps = App.objects.filter(user=self.request.user)

        apps = []
        for app in channels_apps:
            apps.append({
                "id": app.id,
                "name": app.name,
                "channels": list(filter(lambda c: c.app == app, channels))
            })

        context.update({
            "apps": apps
        })
        return context
