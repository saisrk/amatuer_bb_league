from __future__ import unicode_literals

from django.db import models

class Team(models.Model):
    teamname = models.CharField(max_length=100, verbose_name="Team Name")

    def __unicode__(self):
        return self.teamname

class Player(models.Model):
    pfirstname = models.CharField(max_length=100, verbose_name='Player First Name')
    plastname = models.CharField(max_length=100, verbose_name='Player Last Name')
    pemail = models.EmailField(verbose_name='Player Email')
    mobilenum = models.CharField(max_length=10, verbose_name='Mobile Number')
    teamname = models.ForeignKey(Team)

    def __unicode__(self):
        return "%s %s" % (self.pfirstname, self.plastname)