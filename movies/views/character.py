from rest_framework import generics
from movies.models import Character
from movies.serializers import CharacterMovieSerializer

class PersonCharactersListView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Character.objects\
            .select_related('movie')\
            .filter(person_id=self.kwargs['personId'])
        return queryset

    serializer_class = CharacterMovieSerializer
