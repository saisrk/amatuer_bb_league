from django.shortcuts import render
from django.http import HttpResponseRedirect

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

def add_team(request):
    if request.method == 'POST':
        form = TeamCreateForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            return HttpResponseRedirect('/abl/')
    else:
        teamform = TeamCreateForm()

    return render(request, 'players/add_team_form.html', {'form': teamform})