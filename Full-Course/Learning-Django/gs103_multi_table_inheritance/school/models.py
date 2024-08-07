from django.db import models

# https://docs.djangoproject.com/en/5.0/topics/db/models/#multi-table-inheritance

# The second type of model inheritance supported by Django is when each model in the hierarchy is a model all by itself. 
# Each model corresponds to its own database table and can be queried and created individually. 
# The inheritance relationship introduces links between the child model and each of its parents (via an automatically-created OneToOneField). 


class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)


class Student(ExamCenter):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
