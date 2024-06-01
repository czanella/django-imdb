from rest_framework import generics
from movies.models import CrewMember
from movies.serializers import CrewMemberMovieSerializer

class PersonCrewMembersListView(generics.ListAPIView):
    def get_queryset(self):
        queryset = CrewMember.objects\
            .select_related('movie')\
            .filter(person_id=self.kwargs['personId'])\
            .order_by('movie__year')
        return queryset

    serializer_class = CrewMemberMovieSerializer
