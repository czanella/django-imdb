from rest_framework import serializers
from movies.models import Character
from .person import PreviewPersonSerializer
from .movie import PreviewMovieSerializer

class CharacterPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'name',
            'is_self',
            'person',
        )

    person = PreviewPersonSerializer()


class CharacterMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'name',
            'is_self',
            'movie',
        )

    movie = PreviewMovieSerializer()
