from django.dispatch import Signal, receiver

# Creating Signals
# notification = Signal(providing_args=["request", "user"])
notification = Signal()


# Receiver Function ( when notification signal is sent, our show_notification function will execute)
@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notification")



