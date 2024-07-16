from django.db import models

# see also the admin.py file

# https://docs.djangoproject.com/en/5.0/topics/db/models/#model-inheritance

# Types of model Ingeritance:
# 1) Abstract Base Class and Meta Inheritance
# 2) Multi-Table Inheritance
# 3) Proxy Model

class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        # it becomes an abstract class not a model,so now you can’t generate a database table.
        abstract = True


class Student(CommonInfo):
    fees = models.IntegerField()
    date = None


class Teacher(CommonInfo):
    salary = models.IntegerField()


class Contractor(CommonInfo):
    date = models.DateTimeField()
    payment = models.IntegerField()


# These tables can be implemented by using Abstract Base Class Inheritance i.e., by the above way as we have implemented it
'''
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70) # Same
    age = models.IntegerField() # Same
    fees = models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=70) # Same
    age = models.IntegerField() # Same
    date = models.DateField()
    salary = models.IntegerField()


class Contractor(models.Model):
    name = models.CharField(max_length=70) # Same
    age = models.IntegerField() # Same
    date = models.DateTimeField()
    payment = models.IntegerField()
'''
