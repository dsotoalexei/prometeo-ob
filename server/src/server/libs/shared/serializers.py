from rest_framework import serializers

from .choices import ResponseStatusChoice


class PrometeoResponseSerializer(serializers.Serializer):
    """Serializer for common response
    """
    status = serializers.ChoiceField(choices=ResponseStatusChoice.choices)
    key = serializers.CharField(required=False)
    message = serializers.CharField(required=False)


class KeySerializer(serializers.Serializer):
    """Serializer for validation request parameters
    """
    key = serializers.CharField()
