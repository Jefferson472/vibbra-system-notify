from django.core.mail import EmailMultiAlternatives

from .models.notification import EmailNotification


def send_email_notification(notification: EmailNotification):
    email = EmailMultiAlternatives(
        subject=notification.subject,
        from_email=notification.channel.content_object.sender_email,
        to=notification.recipients.split(',')
    )
    email.attach_alternative(notification.message, "text/html")
    email.send()
