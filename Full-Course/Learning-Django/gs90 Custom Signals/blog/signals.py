from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from django.apps import apps

# Creating Signals
# notification = Signal(providing_args=["request", "user"])
notification = Signal()


# Receiver Function ( when notification signal is sent, our show_notification function will execute)
@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f"{kwargs}")
    print("Notification")


# **********************************

# https://medium.com/@mansha99/django-drf-signals-custom-signals-model-signals-enforcing-business-rules-729fc2e22c7c

# Predefined Model signal receiver
@receiver(post_save, sender="blog.Notice")
def valid_notice_created(sender, instance, created, **kwargs):
    if created:
        message = "Notice Created : id = {id} ".format(id=instance.id)
        print(message)


# Creating custom signal
invalid_notice_signal = Signal()


# Custom signal receiver
@receiver(invalid_notice_signal)
def invalid_notice_created(sender, **kwargs):
    message = "Alert!!! Someone tried to create Invalid notice"
    print(message)
