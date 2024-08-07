from django.dispatch import Signal, receiver

# user_visit_signal = Signal(["date_time", "ip", "device"])
user_visit_signal = Signal()  # work same as above


@receiver(user_visit_signal)
def handle_user_visit(sender, date_time, ip, device, **kwargs):
    message = "Visit to view {sender}, at {date_time} , IP is {ip} , Device is {device}".format(
        sender=sender, date_time=date_time, ip=ip, device=device
    )
    print(message)
