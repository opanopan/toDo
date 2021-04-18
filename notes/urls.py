from django.urls import path, include
from .views import NotesView, NotesView_id

app_name = 'notes'

urlpatterns = [
    path('note/', NotesView.as_view()),
    path('note/<int:note_id>', NotesView_id.as_view()),
]
