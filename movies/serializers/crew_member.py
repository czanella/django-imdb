from rest_framework import serializers
from movies.models import CrewMember
from .person import PreviewPersonSerializer

class CrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = (
            'job',
            'job_category',
            'person',
        )

    person = PreviewPersonSerializer()
