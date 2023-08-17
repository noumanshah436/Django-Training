from django.db import models

import datetime

from django.utils import timezone


# Create your models here.
# https://docs.djangoproject.com/en/4.0/intro/tutorial02/
# https://docs.djangoproject.com/en/4.0/topics/db/queries/#field-lookups-intro

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):  # custom method
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
