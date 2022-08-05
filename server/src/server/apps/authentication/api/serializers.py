from rest_framework import serializers

class AuthSerializer(serializers.Serializer):

    username = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)
    provider = serializers.CharField(read_only=True)


class EmptyPayloadResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()
