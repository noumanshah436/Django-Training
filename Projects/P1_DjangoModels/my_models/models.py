from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)


# one to many relationship
class Artist(models.Model):
    name = models.CharField(
        max_length=200, db_index=True, help_text='Artist name')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Album(models.Model):
    title = models.CharField(
        max_length=200, db_index=True, help_text='Album title')
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=200, db_index=True,
                            help_text='Genre of music (i.e. Blues)')

    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.CharField(
        max_length=200, db_index=True, help_text='Track title')
    rating = models.IntegerField(null=True)
    length = models.IntegerField(null=True)
    count = models.IntegerField(null=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


# ****************************************
# relationships
# ****************************************
class Person(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField(null=True)
    mobile = models.TextField(max_length=100)

    def __str__(self):
        return self.name
        # return f"name: {self.name}, email: {self.email}"


# one to many relationship
# Each person can hold more than one account
class Account(models.Model):
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    account_number = models.TextField()
    balance = models.TextField(max_length=100)


# One to One Relationship
# A person can have only one Adhar ID
class Adhar(models.Model):
    person = models.OneToOneField("Person", on_delete=models.CASCADE)
    signature = models.TextField(null=True)
    adhar_no = models.TextField(max_length=100)


# many to many relationship
# Each customer can be related to n number of products and
#  each product can be linked to n number of customers.
class Customer(models.Model):
    cus_name = models.TextField(max_length=100)
    cus_email = models.EmailField()
    cus_mobile = models.TextField(max_length=100)


class Product(models.Model):
    customers = models.ManyToManyField("Customer")
    cus_name = models.TextField()
    cus_qty = models.TextField(max_length=100)
