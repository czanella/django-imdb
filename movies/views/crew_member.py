from rest_framework import mixins, viewsets
from movies.models import CrewMember
from movies.serializers import CrewMemberMovieSerializer

class PersonCrewMemberViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    def get_queryset(self):
        queryset = CrewMember.objects\
            .select_related('movie')\
            .filter(person_id=self.kwargs['personId'])\
            .order_by('movie__year')
        return queryset

    serializer_class = CrewMemberMovieSerializer
