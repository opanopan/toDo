from rest_framework.serializers import ModelSerializer, Serializer, ListField, ChoiceField, NullBooleanField

from .models import Notes


class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'


class QuerySerializer(Serializer):
    state = ListField(child=ChoiceField(choices=Notes.NOTE_STATES), required=False)
    is_important = NullBooleanField(required=False, default=None)
    is_public = NullBooleanField(required=False, default=None)
