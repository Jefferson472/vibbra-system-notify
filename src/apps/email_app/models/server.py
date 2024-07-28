from django.db import models

from apps.users.models import User


class ServerConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, unique=True)
    smtp_server = models.CharField(max_length=255)
    smtp_port = models.PositiveIntegerField()
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # TODO: Encryption required
    sender_name = models.CharField(max_length=255)
    sender_email = models.EmailField()

    def __str__(self):
        return self.name
