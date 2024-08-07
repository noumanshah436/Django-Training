from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

# Methods that return new QuerySets: (https://docs.djangoproject.com/en/5.0/ref/models/querysets/#methods-that-return-new-querysets)

# Django provides a range of QuerySet refinement methods that modify either the types of results returned by the QuerySet or the way its SQL query is executed.
# Note
# These methods do not run database queries, therefore they are safe to run in asynchronous code, and do not have separate asynchronous versions.

def home(request):
    student_data = Student.objects.all()

    # student_data = Student.objects.filter(marks=70)
    
    # student_data = Student.objects.exclude(marks=70)
    # ****************************************************************

    # student_data = Student.objects.order_by('?') # '?[for random]', 'name', 'roll', ''marks
    # student_data = Student.objects.order_by('marks') #  ascending order
    # student_data = Student.objects.order_by('-name') #  descending order

    # student_data = Student.objects.order_by('id').reverse()
    # to get last five records:
    # student_data = Student.objects.order_by('id').reverse()[:5]  
    # ****************************************************************

    # values(): Returns a QuerySet that returns dictionaries, rather than model instances, when used as an iterable.
    # student_data = Student.objects.values()               # return all columns in dictionary
    # student_data = Student.objects.values('name', 'city') # return only selected columns
    # ****************************************************************

    # values_list(): This is similar to values() except that instead of returning dictionaries, it returns tuples when iterated over.
    # student_data = Student.objects.values_list()
    # student_data = Student.objects.values_list('name', 'city')
    # student_data = Student.objects.values_list('id', 'name', named=True)

    # ****************************************************************

    # using(alias):
    # This method is for controlling which database the QuerySet will be evaluated against if you are using more than one database. 
    # The only argument this method takes is the alias of a database, as defined in DATABASES.
    
    # student_data = Student.objects.using('default')

    # ****************************************************************

    # student_data = Student.objects.dates('pass_date', 'year')

    # ****************************************************************

    # Uses SQL’s UNION operator to combine the results of two or more QuerySets.  
    # use same number of columns for all querysets

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1, all=True)

    # ****************************************************************

    # intersection
    # Uses SQL’s INTERSECT operator to return the shared elements of two or more QuerySets.
    # Return only those records where the values of all the selected coulumns of both quesrysets are same

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.intersection(qs1)

    # return records where id and name of both querysets are same

    # ****************************************************************

    # difference()
    # Uses SQL’s EXCEPT operator to keep only elements present in the QuerySet but not in some other QuerySets.

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.difference(qs1)

    # return all the records of qs1, that do not match with any record of qs2

    # ****************************************************************

    #  AND OR operator  
    # student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(id=6, roll=106)
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106))

    # student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=107)
    # student_data = Student.objects.filter(Q(id=6) | Q(roll=107))

    print("Return: ", student_data)
    print("SQL Query: ", student_data.query) # To get the respected sql query
    return render(request, 'school/home.html', {'students': student_data})
