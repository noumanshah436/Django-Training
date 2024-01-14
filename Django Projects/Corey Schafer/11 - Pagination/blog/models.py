from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # on_delete : if the user is deleted , then we want to delete their posts as well

    def __str__(self):  # dunder(double underscore) str method
        return self.title

    # get_absolute_url allow the view to handle the redirect for us
    def get_absolute_url(self):
        # reverse returns the location(route url) of the specific object of the post as a string
        return reverse('post-detail', kwargs={'pk': self.pk})


# DateTimeField(auto_now = True)   -> for last modified field
# DateTimeField(auto_now-add = True)   -> save current date when object is created but we cannot modify that date

"""

Any time we make change to our model this is also going make change to the database, 
and need to run these migrations for those changes to take effect

python manage.py makemigrations 
python manage.py migrate 

***********************

get_absolute_url():

Define a get_absolute_url() method to tell Django how to calculate the canonical URL for an object.
 To callers, this method should appear to return a string that can be used to refer to the object over HTTP.

For example:

def get_absolute_url(self):
    return "/people/%i/" % self.id

"""
