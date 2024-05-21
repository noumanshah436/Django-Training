# blog/models.py
from django.db import models
from blog.signals import invalid_notice_signal


class Notice(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.title == "Oops":
            invalid_notice_signal.send(sender=None)
            return
        else:
            super().save(*args, **kwargs)


# Test signals in shell

# python manage.py shell

# >>> from blog.models import Notice

# >>> Notice.objects.create(title="This is valid title", description="My desc")
# Notice Created : id = 1
# <Notice: Notice object (1)>

# >>> Notice.objects.create(title="Oops", description="My desc")
# Alert!!! Someone tried to create Invalid notice
# <Notice: Notice object (None)>
