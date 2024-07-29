from django.urls import path

from .views.notification import (
    EmailNotificationCreateView,
    NotificationDetailView,
    NotificationHistoryView,
)
from .views.server import EmailServerConfigCreateView
from .views.template import EmailTemplateUploadView


urlpatterns = [
     path('email/server/create', EmailServerConfigCreateView.as_view(),
          name='server_config_create'),
     path('email/template/create', EmailTemplateUploadView.as_view(),
          name='email_template_upload'),
     path('send-email/<int:channel_id>', EmailNotificationCreateView.as_view(),
          name='send_email_notification'),
     path('notification-history/', NotificationHistoryView.as_view(),
          name='notification_history'),
     path('notification/<int:pk>/', NotificationDetailView.as_view(),
          name='notification_detail'),
]
