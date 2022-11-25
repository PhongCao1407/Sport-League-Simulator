from django.db import models
from .league import Leagues

class Teams(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    league = models.ForeignKey(Leagues, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'teams'
        unique_together = (('name', 'league'),)