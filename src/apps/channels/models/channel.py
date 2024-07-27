from django.db import models

from apps.channels.models.app import App


class Channel(models.Model):
    CHANNEL_TYPES = [
        ('web_push', 'Web Push'),
        ('email', 'E-mail'),
        ('sms', 'SMS')
    ]

    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='channels')
    channel_type = models.CharField(max_length=50, choices=CHANNEL_TYPES)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_channel_type_display()} for {self.app.name}"
