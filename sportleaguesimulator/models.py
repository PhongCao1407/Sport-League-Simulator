# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AwayTeams(models.Model):
    teams = models.OneToOneField('Teams', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'away_teams'


class GameDays(models.Model):
    seasons_year = models.OneToOneField('Seasons', models.DO_NOTHING, db_column='seasons_year', primary_key=True)
    league_id = models.IntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'game_days'
        unique_together = (('seasons_year', 'date', 'league_id'),)


class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    season_year = models.ForeignKey(GameDays, models.DO_NOTHING, db_column='season_year')
    date = models.DateField()
    league_id = models.IntegerField()
    home_team = models.ForeignKey('HomeTeams', models.DO_NOTHING)
    away_team = models.ForeignKey(AwayTeams, models.DO_NOTHING)
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'games'


class HomeTeams(models.Model):
    teams = models.OneToOneField('Teams', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'home_teams'


class Leagues(models.Model):
    sport = models.ForeignKey('Sports', models.DO_NOTHING, db_column='sport')
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'leagues'
        unique_together = (('sport', 'name'),)


class PlayerStatistics(models.Model):
    player = models.OneToOneField('Players', models.DO_NOTHING, primary_key=True)
    game = models.ForeignKey(Games, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'player_statistics'
        unique_together = (('player', 'game'),)


class Players(models.Model):
    player_id = models.IntegerField(primary_key=True)
    jersey_number = models.IntegerField()
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    teams = models.ForeignKey('Teams', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'players'


class Seasons(models.Model):
    year = models.IntegerField(primary_key=True)
    league = models.ForeignKey(Leagues, models.DO_NOTHING)
    number_of_games = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seasons'
        unique_together = (('year', 'league'),)


class Sports(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'sports'


class TeamRecords(models.Model):
    season_year = models.OneToOneField(Seasons, models.DO_NOTHING, db_column='season_year', primary_key=True)
    league_id = models.IntegerField()
    team = models.ForeignKey('Teams', models.DO_NOTHING)
    win = models.IntegerField()
    loss = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_records'
        unique_together = (('season_year', 'league_id', 'team'),)


class Teams(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    league = models.ForeignKey(Leagues, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'teams'
        unique_together = (('name', 'league'),)
