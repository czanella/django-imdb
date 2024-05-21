from rest_framework import serializers
from movies.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'id',
            'name',
            'is_self',
        )
