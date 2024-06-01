from rest_framework import serializers
from movies.models import Character
from .person import PreviewPersonSerializer

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'name',
            'is_self',
            'person',
        )

    person = PreviewPersonSerializer()
