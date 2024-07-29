from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.channels.models.app import App
from apps.email_app.models.template import Template


class Channel(models.Model):
    CHANNEL_TYPES = [
        ('web_push', 'Web Push'),
        ('email', 'E-mail'),
        ('sms', 'SMS')
    ]

    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='channels')
    name = models.CharField(max_length=55, verbose_name="Nome")
    channel_type = models.CharField(max_length=50, choices=CHANNEL_TYPES,
                                    verbose_name="Tipo de Canal")
    enabled = models.BooleanField(default=True)
    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={'model__in': ('web_push', 'email', 'sms')},
        on_delete=models.SET_NULL,
        null=True
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.get_channel_type_display()} - App: {self.app.name}"
