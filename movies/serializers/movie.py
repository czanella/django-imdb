from rest_framework import serializers
from movies.models import Movie
from .character import CharacterSerializer

class ListMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'url',
            'primary_title',
        )


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'tconst',
            'type',
            'primary_title',
            'original_title',
            'year',
            'runtime',
            'rating',
            'rating_votes',
            'imdb_url',
            'characters',
        )

    characters = CharacterSerializer(many=True)
