from django.db import models

# Create your models here.
class Player(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  contact = models.CharField(max_length=20)
  age = models.IntegerField()
  number = models.IntegerField()
  position = models.CharField(max_length=20)
  status = models.CharField(max_length=20)
  team_id = models.ForeignKey('Team', related_name='players', blank=True, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'This players name is {self.first_name} {self.last_name}'
  
