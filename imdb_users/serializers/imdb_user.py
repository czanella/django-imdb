from rest_framework import serializers
from imdb_users.models import ImdbUser

class ImdbUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImdbUser
        fields = [
            'id',
            'email',
            'is_staff',
        ]
