from rest_framework import serializers


class ProviderSerializer(serializers.Serializer):
    """Serializer for Provider
    """
    code = serializers.CharField()
    name = serializers.CharField()
    country = serializers.CharField()


class ProviderResponseSerializer(serializers.Serializer):
    """Serializer for Provider
    """
    status = serializers.CharField()
    providers = ProviderSerializer(many=True)

