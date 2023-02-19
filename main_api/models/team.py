from django.db import models

# Create your models here.
class Team(models.Model):
  city = models.CharField(max_length=50)
  mascot = models.CharField(max_length=50)
  logo_url = models.CharField(max_length=200)
  team_color = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.city} {self.team_name}'
