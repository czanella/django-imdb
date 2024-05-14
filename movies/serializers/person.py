from rest_framework import serializers
from movies.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'nconst',
            'name',
            'year_of_birth',
            'year_of_death',
            'url',
        )
