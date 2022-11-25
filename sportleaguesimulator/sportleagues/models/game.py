from django.db import models
from .gameday import GameDays
from .hometeam import HomeTeams
from .awayteam import AwayTeams

class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    season_year = models.ForeignKey(GameDays, models.DO_NOTHING, db_column='season_year')
    date = models.DateField()
    league_id = models.IntegerField()
    home_team = models.ForeignKey(HomeTeams, models.DO_NOTHING)
    away_team = models.ForeignKey(AwayTeams, models.DO_NOTHING)
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'games'