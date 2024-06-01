from rest_framework import serializers
from movies.models import Movie
from .character import CharacterPersonSerializer
from .crew_member import CrewMemberPersonSerializer

class PreviewMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'url',
            'primary_title',
            'original_title',
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
            'crew_members',
        )

    characters = CharacterPersonSerializer(many=True)
    crew_members = CrewMemberPersonSerializer(many=True)