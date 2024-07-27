from django.db import models

from apps.users.models import User


class App(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Nome")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
