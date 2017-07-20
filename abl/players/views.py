from django.views.generic import (ListView,
                                  DeleteView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  )

from .models import Player, Team
from .forms import PlayerCreateForm, TeamCreateForm

# Creating Player and Parent
class PlayerCreateView(CreateView):
    form_class = PlayerCreateForm
    template_name = "players/player_form.html"

class ParentCreateView(CreateView):
    form_class = TeamCreateForm
    template_name = "players/parent_form.html"

# Modify Player / Parent details
class PlayerUpdateView(UpdateView):
    pass
# List Player details
class PlayerListView(ListView):
    model = Player

# Player Detail
class PlayerDetailView(DetailView):
    model = Player

# Delete Player and Parent details

def index(request):
    return HttpResponse("Under construction")
