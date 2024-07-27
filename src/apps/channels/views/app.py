from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import reverse
from django.views.generic import CreateView

from apps.channels.models import App


class AppView(LoginRequiredMixin, CreateView):
    model = App
    fields = ["name"]
    template_name = "app/app_form.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        app = self.object
        return reverse('channels_list', kwargs={'app_id': app.id})
