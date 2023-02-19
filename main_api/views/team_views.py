from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.team import Team
from ..serializers import TeamSerializer

# Create your views here.
class TeamClass(APIView):
    def get(self, request):
        """Index Request"""
        print(request.session)
        teams = Team.objects.all()[:10]
        data = TeamSerializer(teams, many=True).data
        return Response(data)

    serializer_class = TeamSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        team = TeamSerializer(data=request.data)
        if team.is_valid():
            b = team.save()
            return Response(team.data, status=status.HTTP_201_CREATED)
        else:
            return Response(team.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        team = get_object_or_404(Team, pk=pk)
        data = TeamSerializer(team).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        team = get_object_or_404(Team, pk=pk)
        ms = TeamSerializer(team, data=request.data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        team = get_object_or_404(Team, pk=pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)