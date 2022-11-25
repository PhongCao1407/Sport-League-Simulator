from django.db import models
from .sport import Sports

class Leagues(models.Model):
    sport = models.ForeignKey(Sports, models.DO_NOTHING, db_column='sport')
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'leagues'
        unique_together = (('sport', 'name'),)