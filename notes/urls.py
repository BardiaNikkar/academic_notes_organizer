from django.urls import path
from .views import create_note, note_list, update_note

urlpatterns = [
    path('create/', create_note, name='note_create'),
    path('', note_list, name='note_list'),
    path('<int:pk>/update/', update_note, name='note_update'),
]