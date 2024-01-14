from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete=models.CASCADE
    # if the user is deleted , then we want to delete their posts as well

    def __str__(self):  # dunder(double underscore) str method
        return self.title

# DateTimeField(auto_now = True) = for last modified field

# DateTimeField(auto_now-add = True)  =
# save current date when object is created but we cannot modify that date


CAR_COLOR_CHOICES = (
    ("red", "Red"),
    ("blue", "Blue"),
    ("green", "Green"),
    ("yellow", "Yellow"),
    ("black", "Black"),
    ("white", "White"),
)


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    model = models.DateField()
    color = models.CharField(
        max_length=20,
        choices=CAR_COLOR_CHOICES,
        default="black"
    )

    def __str__(self):
        return self.name
