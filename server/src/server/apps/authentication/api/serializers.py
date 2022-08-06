from rest_framework import serializers


class LoginRequestSerializer(serializers.Serializer):
    """Serializer for login request
    """
    provider = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    type = serializers.CharField(required=False)

