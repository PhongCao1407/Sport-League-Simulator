from django.db import models
from .team import Teams

class Players(models.Model):
    player_id = models.IntegerField(primary_key=True)
    jersey_number = models.IntegerField()
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    team = models.ForeignKey(Teams, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'players'