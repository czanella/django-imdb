from rest_framework import serializers
from movies.models import Character
from .movie import PreviewMovieSerializer

class CharacterMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'name',
            'is_self',
            'movie',
        )

    movie = PreviewMovieSerializer()
