from django.db import models
from .league import Leagues


class Seasons(models.Model):
    year = models.IntegerField(primary_key=True)
    league = models.ForeignKey(Leagues, models.DO_NOTHING)
    number_of_games = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'seasons'
        unique_together = (('year', 'league'),)