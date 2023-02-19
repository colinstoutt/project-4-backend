from django.urls import path
from .views.player_views import Player, PlayerDetail
from .views.team_views import TeamClass, TeamDetail
from .views.game_views import Game, GameDetail
from .views.recruit_views import Recruit, RecruitDetail


urlpatterns = [
    path('player/', Player.as_view(), name='player'),
    path('player/<int:pk>/', PlayerDetail.as_view(), name='player_detail'),
    path('recruit/', TeamClass.as_view(), name='recruit'),
    path('recruit/<int:pk>/', TeamDetail.as_view(), name='recruit_detail'),
    path('game/', TeamClass.as_view(), name='game'),
    path('game/<int:pk>/', TeamDetail.as_view(), name='game_detail'),
    path('team/', TeamClass.as_view(), name='team'),
    path('team/<int:pk>/', TeamDetail.as_view(), name='team_detail')
]