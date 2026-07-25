from django.urls import path
from .views import create_course, course_list, update_course, delete_course

urlpatterns = [
    path('create/', create_course, name='course_create'),
    path('', course_list, name='course_list'),
    path('<int:pk>/update/', update_course, name='course_update'),
    path('<int:pk>/delete/', delete_course, name='course_delete'),
]
