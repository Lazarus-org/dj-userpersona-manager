from rest_framework import serializers

from persona_manager.models import UserPersona


class UserPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPersona
        fields = "__all__"  # Include all fields from the model
