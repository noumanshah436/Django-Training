from django.db import models

# an Article can be published in multiple Publication objects,
# and a Publication has multiple Article objects:


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"id: {self.id}, headline: {self.title}"


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return f"id: {self.id}, headline: {self.headline}"


# ****************************************
# Extra fields on many-to-many relationships
# ****************************************

# Person ←→ Membership ←→ Group

# A person can be a member of multiple groups and a group can have multiple members.
# Each instance of Person can be associated with multiple instances of Group, and each instance of Group can be associated with multiple instances of Person.
# The Membership model is used as an intermediary table that not only connects Person and Group but also allows you to store additional information about the relationship between the two, such as when the person joined the group and the reason for the invitation.


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"id: {self.id}, headline: {self.name}"


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return f"id: {self.id}, headline: {self.name}"


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
