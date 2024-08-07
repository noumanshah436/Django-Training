import os

from django.core.mail import (
    send_mail,
    EmailMessage,
    mail_admins,
    mail_managers,
    EmailMultiAlternatives,
)
from django.template.loader import render_to_string
from django.conf import settings


def send_email():
    subject = "Hello from Django"
    message = "This is a test email sent from Django."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [
        "noumanshah436@gmail.com",
    ]

    send_mail(subject, message, from_email, recipient_list)


def send_email_with_attachment():
    subject = "Welcome Email"
    message = "This is a test email sent from Django."
    recipient_list = [
        "noumanshah436@gmail.com",
    ]
    file_path = os.path.join(settings.BASE_DIR, "sample.png")

    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=recipient_list,
    )

    mail.attach_file(file_path)

    # To use `attach` method, we can attach like below:
    # with open(file_path, 'rb') as f:
    #     email.attach('sample.png', f.read(), 'image/png')

    mail.send()


def notify_admins():
    subject = "Critical Error"
    message = "A critical error occurred on the site."
    mail_admins(subject, message)


def notify_managers():
    subject = "Important Notification"
    message = "An important event has occurred on the site."
    mail_managers(subject, message)


def send_templated_email():
    # https://docs.djangoproject.com/en/5.0/topics/email/#sending-alternative-content-types
    subject = "Test Email with Template"
    from_email = settings.EMAIL_HOST_USER
    to_email = "noumanshah436@gmail.com"

    # Define the context for the template
    context = {
        "subject": subject,
        "body": "This is a test email with a template.",
    }

    # Load and render the templates
    text_content = render_to_string("enroll/email_template.txt", context)
    html_content = render_to_string("enroll/email_template.html", context)

    # Create the email message
    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")

    # Attach the file
    file_path = os.path.join(settings.BASE_DIR, "sample.png")
    email.attach_file(file_path)

    # Send the email
    email.send()
