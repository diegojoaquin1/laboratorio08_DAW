from rest_framework import serializers
from ..models import PlayerTournament

class PlayerTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerTournament
        fields = '__all__'
        read_only_fields = ('created', 'modified')
