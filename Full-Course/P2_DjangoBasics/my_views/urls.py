from django.urls import path
from . import views

app_name = "my_views"
urlpatterns = [
    path('', views.index, name="index"),
    path('index2/', views.index2, name="index2"),
    path('index3/', views.index3, name="index3"),
    path('build_in_tags_and_filters/', views.build_in_tags_and_filters,
         name="build_in_tags_and_filters"),
    path('posts/', views.display_posts, name="posts"),
    path('user/<int:id>', views.get_user_by_id, name="get_user"),
    path('newpost/', views.new_post, name="newpost"),

    path("cars/", views.MyCarsIndexView.as_view(), name="car_index"),
    path("car/<int:pk>/", views.MyCarDetailView.as_view(), name="car_detail"),
]
