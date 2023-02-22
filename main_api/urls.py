from django.urls import path
from .views.player_views import PlayerClass, PlayerDetail
from .views.team_views import TeamClass, TeamDetail
from .views.game_views import GameClass, GameDetail
from .views.recruit_views import RecruitClass, RecruitDetail


urlpatterns = [
    path('player/', PlayerClass.as_view(), name='player'),
    path('player/<int:pk>/', PlayerDetail.as_view(), name='player_detail'),
    path('recruit/', RecruitClass.as_view(), name='recruit'),
    path('recruit/<int:pk>/', RecruitDetail.as_view(), name='recruit_detail'),
    path('game/', GameClass.as_view(), name='game'),
    path('game/<int:pk>/', GameDetail.as_view(), name='game_detail'),
    path('team/', TeamClass.as_view(), name='team'),
    path('team/<int:pk>/', TeamDetail.as_view(), name='team_detail')
]