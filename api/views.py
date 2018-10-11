from rest_framework.generics import ListCreateAPIView
from notes.models import Note
from api.serializers import NoteSerializer


class NoteListCreateAPIView(ListCreateAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        order = self.request.query_params.get('order')
        if order == 'dec':
            return Note.objects.order_by('-unique_words', 'created_date')
        return Note.objects.order_by('unique_words', 'created_date')
