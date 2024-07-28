from django.urls import path

from .views.server import EmailServerConfigCreateView
from .views.template import EmailTemplateUploadView


urlpatterns = [
    path('email/server/create', EmailServerConfigCreateView.as_view(),
         name='server_config_create'),
    path('email/template/create', EmailTemplateUploadView.as_view(),
         name='email_template_upload'),
]
