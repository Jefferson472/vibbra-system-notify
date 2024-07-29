import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apps.email_app.models import EmailNotification


def send_email_notification(notification: EmailNotification):
    server_config = notification.channel.content_object

    msg = MIMEMultipart('alternative')
    msg['Subject'] = notification.subject
    msg['From'] = server_config.sender_email
    msg['To'] = notification.recipients

    part = MIMEText(notification.message, 'html')
    msg.attach(part)

    try:
        server = smtplib.SMTP(server_config.smtp_server, server_config.smtp_port)
        server.starttls()
        server.login(server_config.login, server_config.password)
        server.sendmail(server_config.sender_email, notification.recipients.split(','), msg.as_string())
        server.quit()

        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
