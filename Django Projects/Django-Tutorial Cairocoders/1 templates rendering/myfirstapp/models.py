from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Contact(models.Model):
    firstName = models.CharField("First name", max_length=255, blank=True, null=True)
    lastName = models.CharField("Last name", max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.firstName


class Post(models.Model):
    # models.ForeignKey – this is a link to another model.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # models.TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
    text = models.TextField()
    # models.DateTimeField – this is a date and time.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# python manage.py makemigrations myfirstapp
# python manage.py migrate
