from django import forms

from .models import EmailNotification, ServerConfig, Template


class ServerConfigForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ServerConfig
        fields = [
            'name',
            'smtp_server',
            'smtp_port',
            'login',
            'password',
            'sender_name',
            'sender_email'
        ]


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'template_file']
        widgets = {
            'template_file': forms.ClearableFileInput(attrs={'accept': '.html'})
        }


class EmailNotificationForm(forms.ModelForm):
    class Meta:
        model = EmailNotification
        fields = ['channel', 'recipients', 'subject', 'template']
