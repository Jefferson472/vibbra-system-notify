from datetime import datetime
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import Context
from django.template import Template as DjangoTemplate
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, ListView

from apps.channels.models.channel import Channel
from apps.email_app.forms import EmailNotificationForm
from apps.email_app.models import EmailNotification
from apps.email_app.models.template import Template
from apps.email_app.tasks import send_email_notification


class EmailNotificationCreateView(LoginRequiredMixin, CreateView):
    model = EmailNotification
    form_class = EmailNotificationForm
    template_name = 'email_app/email_notification_form.html'
    success_url = reverse_lazy('notification_history')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        form = self.get_form()
        form.fields['channel'].queryset = Channel.objects.filter(
            channel_type='email', app__user=self.request.user)
        form.fields['template'].queryset = Template.objects.filter(
            user=self.request.user)

        channel_id = self.kwargs.get('channel_id')
        if channel_id:
            channel = Channel.objects.get(id=channel_id)
            form.fields['channel'].initial = channel
            form.fields['template'].initial = channel.template

        context.update({'form': form})
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user

        with open(form.instance.template.template_file.path, 'r', encoding='utf-8'
                  ) as template_file:
            template_content = template_file.read()
        template = DjangoTemplate(template_content)
        form.instance.message = template.render(Context({}))

        if form.is_valid():
            send_email_notification(notification=form.instance)

        return super().form_valid(form)


class NotificationHistoryView(LoginRequiredMixin, ListView):
    model = EmailNotification
    template_name = 'notification_history.html'
    context_object_name = 'notifications'
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['channels'] = Channel.objects.filter(app__user=self.request.user)
        return context

    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user)

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        channel = self.request.GET.get('channel')
        
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            qs = qs.filter(sent_at__gte=start_date)
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            end_date = end_date + timezone.timedelta(days=1)
            qs = qs.filter(sent_at__lt=end_date)
        if channel:
            qs = qs.filter(channel_id=channel)

        return qs


class NotificationDetailView(DetailView):
    model = EmailNotification
    context_object_name = 'notification'

    def get_object(self):
        notification_id = self.kwargs.get('pk')
        return get_object_or_404(EmailNotification, pk=notification_id)
