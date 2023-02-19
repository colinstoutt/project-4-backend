from django.db import models

# Create your models here.
class Recruit(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  contact = models.CharField(max_length=20)
  age = models.IntegerField()
  hometown = models.CharField(max_length=20)
  position = models.CharField(max_length=20)
  height = models.IntegerField()
  weight = models.IntegerField()
  current_team= models.CharField(max_length=100)
  notes = models.TextField(max_length=500, default='')
  team_id = models.ForeignKey('Team', related_name='recruits', blank=True, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'This recruits name is {self.first_name} {self.last_name}'
