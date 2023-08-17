from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"


# python manage.py makemigrations myfirstapp
# python manage.py migrate myfirstapp
