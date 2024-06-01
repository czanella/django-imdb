from rest_framework import serializers
from movies.models import CrewMember
from .person import PreviewPersonSerializer
from .movie import PreviewMovieSerializer

class CrewMemberPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = (
            'job',
            'job_category',
            'person',
        )

    person = PreviewPersonSerializer()


class CrewMemberMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = (
            'job',
            'job_category',
            'movie',
        )

    movie = PreviewMovieSerializer()
