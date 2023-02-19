from rest_framework import serializers

from .models.player import Player
from .models.team import Team
from .models.game import Game
from .models.recruit import Recruit

class PlayerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Player
    fields = '__all__'
    
class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields = '__all__'
    
class RecruitSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recruit
    fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
  players = PlayerSerializer(many=True, required=False)
  recruits = RecruitSerializer(many=True, required=False)
  games = GameSerializer(many=True, required=False)
  class Meta:
    model = Team
    fields = ('city', "mascot", "team_color", "logo_url", "players", 'recruits', 'games')

