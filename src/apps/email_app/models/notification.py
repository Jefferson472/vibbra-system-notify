from django.db import models

from apps.users.models import User

from .template import Template


class EmailNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipients = models.TextField(verbose_name="Destinatários",
                                  help_text="Separe cada destinatário com vírgula (,)")
    subject = models.CharField(max_length=255, verbose_name="Assunto")
    message = models.TextField(verbose_name="Mensagem", null=True, blank=True)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey('channels.Channel', on_delete=models.SET_NULL,
                                null=True, verbose_name="Canal")

    class Meta:
        ordering = ['-sent_at']
