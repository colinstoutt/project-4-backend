from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.player import Player
from ..serializers import PlayerSerializer

# Create your views here.
class PlayerClass(APIView):
    def get(self, request):
        """Index Request"""
        print(request.session)
        players = Player.objects.all()[:10]
        data = PlayerSerializer(doctors, many=True).data
        return Response(data)

    serializer_class = PlayerSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        player = PlayerSerializer(data=request.data)
        if player.is_valid():
            b = player.save()
            return Response(player.data, status=status.HTTP_201_CREATED)
        else:
            return Response(player.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        player = get_object_or_404(Player, pk=pk)
        data = PlayerSerializer(player).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        player = get_object_or_404(Player, pk=pk)
        ms = PlayerSerializer(player, data=request.data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        player = get_object_or_404(Player, pk=pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
