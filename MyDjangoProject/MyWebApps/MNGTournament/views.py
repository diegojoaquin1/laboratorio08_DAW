from rest_framework import viewsets
from .models import Organizer, Team, Player, Tournament, PlayerTournament
from .serializers import (
    OrganizerSerializer, OrganizerDetailSerializer,
    TeamSerializer, TeamDetailSerializer,
    PlayerSerializer, PlayerDetailSerializer,
    TournamentSerializer, TournamentDetailSerializer,
    PlayerTournamentSerializer, PlayerTournamentDetailSerializer
)

class OrganizerViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizerSerializer

    def get_queryset(self):
        return Organizer.objects.prefetch_related('tournaments').all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrganizerDetailSerializer
        return OrganizerSerializer

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.prefetch_related('players').all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeamDetailSerializer
        return TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.select_related('team').prefetch_related('tournament_registrations').all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PlayerDetailSerializer
        return PlayerSerializer

class TournamentViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentSerializer

    def get_queryset(self):
        return Tournament.objects.select_related('organizer').prefetch_related('player_registrations').all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TournamentDetailSerializer
        return TournamentSerializer

class PlayerTournamentViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerTournamentSerializer

    def get_queryset(self):
        return PlayerTournament.objects.select_related('player', 'tournament').all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PlayerTournamentDetailSerializer
        return PlayerTournamentSerializer
