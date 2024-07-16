from django.db import models

# proxy model 

# Sometimes, you only want to change the Python behavior of a model – perhaps to change the default manager, or add a new method.

# This is what proxy model inheritance is for: creating a proxy for the original model.
# You can create, delete and update instances of the proxy model and all the data will be saved as if you were using the original (non-proxied) model.
# The difference is that you can change things like the default model ordering or the default manager in the proxy, without having to alter the original.


class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)


class MyExamCenter(ExamCenter):
    class Meta:
        # Behave like the same ExamCenter model.
        # No database table created for this model, it uses the base table to store data
        proxy = True
        ordering = ['city']
