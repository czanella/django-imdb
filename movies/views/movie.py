from rest_framework import viewsets, filters
from movies.models import Movie
from movies.serializers import MovieSerializer, ListMovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related('characters', 'characters__person')
    filter_backends = [filters.SearchFilter]
    search_fields = ['primary_title']

    def get_serializer_class(self):
        if self.action == 'list':
            return ListMovieSerializer
        return MovieSerializer
