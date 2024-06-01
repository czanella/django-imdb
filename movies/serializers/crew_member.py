from rest_framework import serializers
from movies.models import CrewMember
from .movie import PreviewMovieSerializer

class CrewMemberMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = (
            'job',
            'job_category',
            'movie',
        )

    movie = PreviewMovieSerializer()
