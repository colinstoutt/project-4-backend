from django.db import models

# Create your models here.
class Game(models.Model):
  location = models.CharField(max_length=50)
  date = models.DateField()
  time = models.CharField(max_length=20)
  home_team = models.CharField(max_length=50)
  away_team = models.CharField(max_length=50)
  team_id = models.ForeignKey('Team', related_name='games', blank=True, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.city} {self.team_name}'
