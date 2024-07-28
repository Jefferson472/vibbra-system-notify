from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.email_app.forms import ServerConfigForm
from apps.email_app.models.server import ServerConfig


class EmailServerConfigCreateView(LoginRequiredMixin, CreateView):
    model = ServerConfig
    form_class = ServerConfigForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
