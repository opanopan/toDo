from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Notes
from .serializers import NotesSerializer


class NotesView(APIView):
    def get(self, request):
        notes_model = Notes.objects.filter(is_public=True)
        product_serializer = NotesSerializer(notes_model, many=True)
        return Response(product_serializer.data)

    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            note_saved = serializer.save()
        return HttpResponse(status=201)


class NotesView_id(APIView):
    def get(self, request, note_id):
        notes_model = Notes.objects.filter(is_public=True, id=note_id)
        product_serializer = NotesSerializer(notes_model, many=True)
        return Response(product_serializer.data)

    def delete(self, request, note_id):
        needed_id = Notes.objects.filter(id=note_id)
        if needed_id:
            needed_id.delete()
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=404)

    def put(self, request, note_id):
        needed_obj = Notes.objects.all()
        serializer = NotesSerializer()
        return serializer.update(needed_obj, note_id)