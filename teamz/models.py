from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=120)
    points = models.DecimalField(max_digits=7, decimal_places=4)
    

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=120)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    games_played = models.DecimalField(max_digits=7, decimal_places=4)

    def __str__(self):
        return self.name

  