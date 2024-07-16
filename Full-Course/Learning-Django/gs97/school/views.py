from django.shortcuts import render
from .models import Student

# Methods that do not return QuerySets (https://docs.djangoproject.com/en/5.0/ref/models/querysets/#methods-that-do-not-return-querysets)

# The following QuerySet methods evaluate the QuerySet and return something other than a QuerySet.

# These methods do not use a cache (see Caching and QuerySets). Rather, they query the database each time they’re called.

# Because these methods evaluate the QuerySet, they are blocking calls, and so their main (synchronous) versions cannot be called from asynchronous code. For this reason, each has a corresponding asynchronous version with an a prefix - for example, rather than get(…) you can await aget(…).


def home(request):
    # get()
    # Returns the object matching the given lookup parameters, which should be in the format described in Field lookups.
    # You should use lookups that are guaranteed unique, such as the primary key or fields in a unique constraint. For example:

    # If get() doesn’t find any object, it raises a Model.DoesNotExist exception:
    # If get() finds more than one object, it raises a Model.MultipleObjectsReturned exception:

    # student_data = Student.objects.get(name='Rohit')
    # student_data = Student.objects.get(id=1)
    student_data = Student.objects.get(pk=1)

    # *******************************************************************

    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()
    # *******************************************************************
    # student_data = Student.objects.last()
    # *******************************************************************
    # student_data = Student.objects.latest('pass_date')
    # *******************************************************************
    # student_data = Student.objects.earliest('pass_date')
    # *******************************************************************
    # student_data = Student.objects.all()
    # print(student_data.exists())

    # student_data = Student.objects.all()
    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())
    # *******************************************************************

    # student_data = Student.objects.create(name="Sameer", roll=114, city="Bokaro", marks=60, pass_date='2020-5-4')

    # student_data, created = Student.objects.get_or_create(name="Sabirr", roll=113, city="Bookaro", marks=90, pass_date='2020-6-4')

    # student_data = Student.objects.filter(id=12).update(name='Kabir', marks=80)
    # student_data = Student.objects.filter(marks=70).update(city="Pass")

    # student_data = Student.objects.update_or_create(id=13, name="Sabirr	", defaults={'name': 'Kohli'})

    # objs = [
    #     Student(name='Sonal', roll=120, city='Dhanbad', marks=40, pass_date='2020-5-4'),
    #     Student(name='Kunal', roll=121, city='Dumka', marks=50, pass_date='2020-5-7'),
    #     Student(name='Anisa', roll=122, city='Giridih', marks=70, pass_date='2020-5-9')
    # ]
    # student_data = Student.objects.bulk_create(objs)

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'BHEL'
    # student_data = Student.objects.bulk_update(all_student_data, ['city'])

    # *******************************************************************
    # Takes a list of field values and the field_name for those values, and returns a dictionary mapping each value to an instance of the object with the given field value
    # by default field name is id if not specified

    # student_data = Student.objects.in_bulk([1, 2])
    # student_data = Student.objects.in_bulk([1, 2], field_name='id') # same as above

    # print(student_data[1].name)
    # student_data = Student.objects.in_bulk([])
    # student_data = Student.objects.in_bulk()

    # *******************************************************************

    # delete single record
    # student_data = Student.objects.get(pk=13).delete()

    # delete all filtered records
    # student_data = Student.objects.filter(marks=50).delete()

    # delete all records
    # student_data = Student.objects.all().delete()

    # *******************************************************************

    # student_data = Student.objects.all()
    # print(student_data.count())

    # *******************************************************************

    print("Return: ", student_data)
    return render(request, 'school/home.html', {'students': student_data})
