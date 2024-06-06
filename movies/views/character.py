from rest_framework import viewsets, mixins
from movies.models import Character
from movies.serializers import CharacterMovieSerializer

class PersonCharactersViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    def get_queryset(self):
        queryset = Character.objects\
            .select_related('movie')\
            .filter(person_id=self.kwargs['personId'])\
            .order_by('movie__year')
        return queryset

    serializer_class = CharacterMovieSerializer
