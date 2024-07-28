from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.db.models.query import QuerySet
from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from apps.channels.forms import ChannelForm
from apps.channels.models.channel import Channel
from apps.email_app.forms import ServerConfigForm, TemplateForm


class ChannelListView(LoginRequiredMixin, ListView):
    model = Channel

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**self.kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset.filter(app__id=self.kwargs.get("app_id"))


class ChannelCreateView(LoginRequiredMixin, CreateView):
    model = Channel
    form_class = ChannelForm
    CONFIGS = {
        "email": ServerConfigForm
    }

    def get_success_url(self) -> str:
        channel = self.object
        return reverse_lazy('channels_list', kwargs={"app_id": channel.app_id})

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**self.kwargs)
        type = self.kwargs.get("type")
        context.update({"config_form": self.CONFIGS[type](prefix='config')})

        if type == "email":
            context.update({"template_form": TemplateForm(prefix='template')})

        return context

    def post(self, request: HttpRequest, *args, **kwargs: Any) -> HttpResponse:
        self.object = None
        type = self.kwargs.get("type")

        form = self.get_form()
        form.instance.app_id = self.kwargs.get("app_id")
        form.instance.channel_type = type

        config_form = self.CONFIGS[type](request.POST, prefix='config')
        config_form.instance.user = request.user

        template_is_valid = True
        if type == "email":
            template_form = TemplateForm(request.POST, request.FILES, prefix='template')
            template_form.instance.user = request.user
            template_is_valid = template_form.is_valid()

        if form.is_valid() and config_form.is_valid() and template_is_valid:
            return self.form_valid(form, config_form, template_form)

        context = self.get_context_data()
        context.update({
            'form': form,
            'config_form': config_form,
            'template_form': template_form
        })
        return self.render_to_response(context)

    def form_valid(self, form: ChannelForm, config_form: ModelForm,
                   template_form: ModelForm = None) -> HttpResponse:
        self.object = form.save(commit=False)
        config_instance = config_form.save()
        template_instance = template_form.save()

        self.object.content_type = ContentType.objects.get_for_model(config_instance)
        self.object.object_id = config_instance.id
        self.object.template = template_instance
        self.object.save()

        return super().form_valid(form)


class ChannelDeleteView(LoginRequiredMixin, DeleteView):
    model = Channel

    def get_success_url(self) -> str:
        channel = self.object
        return reverse_lazy('channels_list', kwargs={"app_id": channel.app_id})
