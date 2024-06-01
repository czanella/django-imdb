from rest_framework import viewsets
from movies.models import Person
from movies.serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.order_by('nconst')
    serializer_class = PersonSerializer
