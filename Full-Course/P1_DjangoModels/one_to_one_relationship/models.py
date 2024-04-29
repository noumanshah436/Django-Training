from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} the place"


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name

# ************************************

# Each user has one prifile and each profile belongs to one user

# class User(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return str(self.name)


# class Profile(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.PROTECT,
#         primary_key=True,
#     )
#     language = models.CharField(max_length=50)
#     email = models.EmailField(max_length=70, blank=True, unique=True)

#     def __str__(self):
#         return str(self.email)