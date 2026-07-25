from django.urls import path
from .views import create_course, course_list

urlpatterns = [
    path('create/', create_course, name='course_create'),
    path('', course_list, name='course_list'),
]
