from django.urls import path, include
# from rest_framework import routers
from . import views
from .views import NotesView, NotesView_id
# router = routers.DefaultRouter()
# router.register(r'notes', views.NotesViewSet)
app_name = 'notes'

#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]



urlpatterns = [
    path('note/', NotesView.as_view()),
    path('note/<int:note_id>', NotesView_id.as_view()),
]