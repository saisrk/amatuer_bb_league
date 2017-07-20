from django import forms

from .models import Player, Team

class PlayerCreateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "pfirstname",
            "plastname",
            "pemail",
            "mobilenum",
            "teamname",
        ]

class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            "teamname",
        ]