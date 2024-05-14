from rest_framework import viewsets
from imdb_users.models import ImdbUser
from imdb_users.serializers import ImdbUserSerializer

class ImdbUserViewSet(viewsets.ModelViewSet):
    queryset = ImdbUser.objects.all()
    serializer_class = ImdbUserSerializer
