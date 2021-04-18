from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.db.models import Q

from .models import Notes
from .serializers import NotesSerializer, QuerySerializer


class NotesView(APIView):

    def get(self, request):
        notes_model = Notes.objects.filter(is_public=True) | Notes.objects.filter(author=request.user.id)
        query_param = QuerySerializer(data=request.query_params)
        if query_param.is_valid():
            print(0)
            q_note = Q()
            print(query_param.data)
            is_im = query_param.data.get('is_important')
            is_pu = query_param.data.get('is_public')
            if is_im is not None:
                q_note &= Q(is_important=is_im)

            if is_pu is not None:
                q_note &= Q(is_public=is_pu)

            if query_param.data.get('state'):
                q_note_state = Q()
                for notes_state in query_param.data['state']:
                    print(1)
                    q_note_state |= Q(state=notes_state)
                q_note &= q_note_state

            print(q_note)
            notes_model = notes_model.filter(q_note)
        else:
            return HttpResponse(status=400)

        return Response(NotesSerializer(notes_model, many=True).data)

    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            note_saved = serializer.save()
        return HttpResponse(status=201)


class NotesView_id(APIView):
    def get(self, request, note_id):
        notes_model = Notes.objects.filter(is_public=True, id=note_id) | \
                      Notes.objects.filter(author=request.user.id, id=note_id)
        product_serializer = NotesSerializer(notes_model, many=True)
        return Response(product_serializer.data)

    def delete(self, request, note_id):
        needed_id = Notes.objects.filter(id=note_id, author=request.user.id)
        if needed_id:
            needed_id.delete()
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=403)

    def put(self, request, note_id):
        saved_note = Notes.objects.filter(id=note_id, author=request.user.id)
        if not saved_note:
            return HttpResponse(status=403)

        serializer = NotesSerializer(saved_note.first(), request.data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=404)
