from django.db import models
from .season import Seasons
from .team import Teams

class TeamRecords(models.Model):
    # Might have to fix this
    season_year = models.OneToOneField(Seasons, models.DO_NOTHING, db_column='season_year', primary_key=True)
    league_id = models.IntegerField()
    team = models.ForeignKey(Teams, models.DO_NOTHING)
    win = models.IntegerField()
    loss = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'team_records'
        unique_together = (('season_year', 'league_id', 'team'),)