from rest_framework import serializers
from movies.models import Character
from .person import PersonSerializer

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'id',
            'name',
            'is_self',
        )

        person = PersonSerializer
