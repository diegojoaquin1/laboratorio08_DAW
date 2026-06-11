from rest_framework import serializers
from ..models import Organizer

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'
        read_only_fields = ('created', 'modified')
