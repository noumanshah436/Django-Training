from django.shortcuts import render
from myceleryproject.celery import add
from myapp.tasks import sub
from celery.result import AsyncResult

# Enqueue Task using delay()
# def index(request):
#     print("Results: ")
#     result1 = add.delay(10, 20)
#     print("Result 1: ", result1)
#     result2 = sub.delay(80, 10)
#     print("Result 2: ", result2)
#     return render(request, "myapp/home.html")

# # Enqueue Task using apply_async()
# def index(request):
#     print("Results: ")
#     result1 = add.apply_async(args=[10, 20])
#     print("Result 1: ", result1)
#     result2 = sub.apply_async(args=[80, 10])
#     print("Result 2: ", result2)
#     return render(request, "myapp/home.html")

# Display addition value after task execution


def index(request):
    # when we hit this url, this will add a new task, that will be received by celery worker for execution
    result = add.delay(10, 30)
    print("Ready: ", result.ready())
    print("Successful: ", result.successful())
    print("Failed: ", result.failed())
    return render(request, "myapp/home.html", {'result': result})


def check_result(request, task_id):
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)
    # print("Ready: ", result.ready())
    # print("Successful: ", result.successful())
    # print("Failed: ", result.failed())

    # # get method blocks the execution, and return the result once the task is completed
    # print("Get: ", result.get()) 
    return render(request, 'myapp/result.html', {'result': result})


def about(request):
    return render(request, 'myapp/about.html')


def contact(request):
    return render(request, 'myapp/contact.html')
