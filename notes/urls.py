from django.urls import path, include
from .views import NotesView, NotesViewId, AboutView

app_name = 'notes'

urlpatterns = [
    path('note/', NotesView.as_view()),
    path('note/<int:note_id>', NotesViewId.as_view()),
    path('note/about', AboutView.as_view()),
]
