from rest_framework import serializers

from .choices import ResponseStatusChoice


class PrometeoResponseSerializer(serializers.Serializer):
    """Serializer for login response
    """
    status = serializers.ChoiceField(choices=ResponseStatusChoice.choices)
    key = serializers.CharField(required=False)
    message = serializers.CharField(required=False)


class KeySerializer(serializers.Serializer):
    """Serializer for validation request
    """
    key = serializers.CharField()
