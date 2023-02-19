from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.game import Game
from ..serializers import GameSerializer

# Create your views here.
class Game(APIView):
    def get(self, request):
        """Index Request"""
        print(request.session)
        games = Game.objects.all()[:10]
        data = GameSerializer(games, many=True).data
        return Response(data)

    serializer_class = GameSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        game = GameSerializer(data=request.data)
        if game.is_valid():
            b = game.save()
            return Response(game.data, status=status.HTTP_201_CREATED)
        else:
            return Response(game.errors, status=status.HTTP_400_BAD_REQUEST)

class GameDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        game = get_object_or_404(Game, pk=pk)
        data = GameSerializer(game).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        game = get_object_or_404(Game, pk=pk)
        ms = GameSerializer(game, data=request.data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        game = get_object_or_404(Game, pk=pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)