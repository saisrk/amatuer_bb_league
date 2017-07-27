from __future__ import unicode_literals

from django.db import models


class Tournament(models.Model):
    tname = models.CharField(max_length=100, verbose_name="Tournament Name")
    maxteams = models.IntegerField(default=0, verbose_name="Max Teams")
    ttype = models.CharField(verbose_name="Tournament Type", max_length=100)

    def __unicode__(self):
        return self.tname

class Team(models.Model):
    teamname = models.CharField(max_length=100, verbose_name="Team Name")
    tournament = models.ForeignKey(Tournament)

    def __unicode__(self):
        return self.teamname

class Match(models.Model):
    homematch = models.CharField(max_length=100)
    awaymatch = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament)
    result = models.CharField(max_length=10)

    def __unicode__(self):
        return "%s vs %s" % (self.homematch, self.awaymatch)

class Player(models.Model):
    pfirstname = models.CharField(max_length=100, verbose_name='Player First Name')
    plastname = models.CharField(max_length=100, verbose_name='Player Last Name')
    pemail = models.EmailField(verbose_name='Player Email', blank=True, null=True)
    mobilenum = models.CharField(max_length=10, verbose_name='Mobile Number', blank=True, null=True)
    playernum = models.IntegerField(default=0)
    teamname = models.ForeignKey(Team)

    def __unicode__(self):
        return "%s %s" % (self.pfirstname, self.plastname)

class PlayerStat(models.Model):
    player = models.OneToOneField(Player)
    match = models.ForeignKey(Match)
    points = models.IntegerField(default=0)
    rebounds = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s got %d points" % (self.player, self.points)