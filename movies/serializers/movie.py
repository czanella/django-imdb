from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'tconst',
            'type',
            'primary_title',
            'original_title',
            'year',
            'runtime',
            'rating',
            'rating_votes',
            'url',
        )
