from django.shortcuts import render

from .models import Player, Team, Tournament, PlayerStat, Match
from .forms import PlayerCreateForm, TeamCreateForm


def index(request):
    tournaments = Tournament.objects.all()
    context_data = {
        "tournaments": tournaments,
    }
    return render(request, 'players/home_page.html', context_data)

def tournament_detail(request, tid):
    tournament = Tournament.objects.get(pk=tid)
    teams_registered = Team.objects.filter(tournament=tournament)
    context_data = {
        "tournament": tournament,
        "teams": teams_registered,
    }
    return render(request, 'players/tournament_detail.html', context_data)