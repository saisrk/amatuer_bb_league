from django.conf.urls import url, include

from .views import index, tournament_detail, add_team

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'(?P<tid>\d+)/', tournament_detail, name='detail'),
    url(r'addteam/', add_team, name='add'),
]