from django.contrib import admin

# Register your models here.
from .models import Team, Player, Match, Tournament, PlayerStat

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Tournament)
admin.site.register(PlayerStat)