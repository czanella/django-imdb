from django.db.models import Prefetch
from rest_framework import viewsets, filters
from movies.models import Movie, Character, CrewMember
from movies.serializers import MovieSerializer, PreviewMovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects\
        .prefetch_related(
            Prefetch('characters', queryset=Character.objects.order_by('ordering')),
            'characters__person',
            Prefetch('crew_members', queryset=CrewMember.objects.order_by('ordering')),
            'crew_members__person',
        )\
        .order_by('year')
    filter_backends = [filters.SearchFilter]
    search_fields = ['primary_title', 'original_title']

    def get_serializer_class(self):
        if self.action == 'list':
            return PreviewMovieSerializer
        return MovieSerializer
