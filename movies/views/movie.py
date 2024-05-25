from rest_framework import viewsets
from movies.models import Movie
from movies.serializers import MovieSerializer, ListMovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Movie.objects.prefetch_related('characters', 'characters__person')
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ListMovieSerializer
        return MovieSerializer
