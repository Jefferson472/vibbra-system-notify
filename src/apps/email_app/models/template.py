from django.db import models

from apps.users.models import User


class Template(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    template_file = models.FileField(upload_to='email_templates/')

    def __str__(self):
        return self.name
