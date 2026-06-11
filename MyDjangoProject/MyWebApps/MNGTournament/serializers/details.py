from rest_framework import serializers
from ..models import (
    Organizer, Team, Player, Tournament, PlayerTournament
)
from .OrganizerSerializer import OrganizerSerializer
from .TeamSerializer import TeamSerializer
from .PlayerSerializer import PlayerSerializer
from .TournamentSerializer import TournamentSerializer
from .PlayerTournamentSerializer import PlayerTournamentSerializer

class OrganizerDetailSerializer(serializers.ModelSerializer):
    tournaments = TournamentSerializer(many=True, read_only=True)
    class Meta:
        model = Organizer
        fields = '__all__'
        read_only_fields = ('created', 'modified')

class TeamDetailSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('created', 'modified')

class PlayerDetailSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    tournament_registrations = PlayerTournamentSerializer(many=True, read_only=True)
    class Meta:
        model = Player
        fields = '__all__'
        read_only_fields = ('created', 'modified')

class TournamentDetailSerializer(serializers.ModelSerializer):
    organizer = OrganizerSerializer(read_only=True)
    player_registrations = PlayerTournamentSerializer(many=True, read_only=True)
    class Meta:
        model = Tournament
        fields = '__all__'
        read_only_fields = ('created', 'modified')

class PlayerTournamentDetailSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    tournament = TournamentSerializer(read_only=True)
    class Meta:
        model = PlayerTournament
        fields = '__all__'
        read_only_fields = ('created', 'modified')
