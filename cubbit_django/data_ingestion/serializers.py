from rest_framework import serializers
from data_ingestion.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['client_user_id', 'timestamp', 'size', 'time_backend', 'status', 'direction']

