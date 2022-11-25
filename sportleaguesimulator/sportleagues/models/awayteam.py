from django.db import models
from .team import Teams

class AwayTeams(models.Model):
    team = models.OneToOneField(Teams, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = True
        db_table = 'away_teams'