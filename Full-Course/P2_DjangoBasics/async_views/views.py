from django.http import HttpResponse
import time
import asyncio
from .models import Movie, Story
from asgiref.sync import sync_to_async

# https://www.youtube.com/watch?v=YneIutRhmgo

# helper funcs


def get_movies():
    print("prepare to get the movies...")
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print("got all the movies!")


def get_stories():
    print("prepare to get the stories...")
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print("got all the stories!")


@sync_to_async
def get_movies_async():
    print("prepare to get the movies...")
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print("got all the movies!")


@sync_to_async
def get_stories_async():
    print("prepare to get the stories...")
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print("got all the stories!")


# views


# http://localhost:8000/async_views
def home_view(request):
    return HttpResponse("Hello world")


# http://localhost:8000/async_views/sync/
def main_view(request):
    start_time = time.time()
    get_movies()
    get_stories()
    total = time.time() - start_time
    print("total: ", total)
    return HttpResponse("sync")
    # total:  7.0053699016571045


# http://localhost:8000/async_views/async/
async def main_view_async(request):
    start_time = time.time()
    # task1 = asyncio.ensure_future(get_movies_async())
    # task2 = asyncio.ensure_future(get_stories_async())
    # await asyncio.wait([task1, task2])
    await asyncio.gather(get_movies_async(), get_stories_async())
    total = time.time() - start_time
    print("total: ", total)
    return HttpResponse("async")

    # total:  5.002896070480347

# ********************************

def main_view(request):
    start_time = time.time()
    data = []
    url_list