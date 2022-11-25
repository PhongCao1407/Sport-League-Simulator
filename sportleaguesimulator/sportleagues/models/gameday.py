from django.db import models
from .season import Seasons

class GameDays(models.Model):
    seasons_year = models.OneToOneField(Seasons, models.DO_NOTHING, db_column='seasons_year', primary_key=True)
    league_id = models.IntegerField()
    date = models.DateField()

    class Meta:
        managed = True
        db_table = 'game_days'
        unique_together = (('seasons_year', 'date', 'league_id'),)