from rest_framework import serializers
from movies.models import Movie, Character, CrewMember
from .person import PreviewPersonSerializer

class PreviewMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'url',
            'primary_title',
            'original_title',
        )


class CharacterPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'name',
            'is_self',
            'person',
        )

    person = PreviewPersonSerializer()


class CrewMemberPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = (
            'job',
            'job_category',
            'person',
        )

    person = PreviewPersonSerializer()


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