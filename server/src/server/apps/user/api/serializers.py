from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """Serializer for User
    """
    name = serializers.CharField()
    document = serializers.CharField()
    email = serializers.CharField()


class InfoResponseSerializer(serializers.Serializer):
    """Serializer for User information response
    """
    status = serializers.CharField()
    info = UserSerializer(many=False)


class AccountSerializer(serializers.Serializer):
    """Serializer for User
    """
    id = serializers.CharField()
    name = serializers.CharField()
    number = serializers.CharField()
    branch = serializers.CharField(required=False, allow_blank=True)
    currency = serializers.CharField()
    balance = serializers.FloatField()


class AccountResponseSerializer(serializers.Serializer):
    """Serializer for User accounts response
    """
    status = serializers.CharField()
    accounts = AccountSerializer(many=True)


class CreditCardSerializer(serializers.Serializer):
    """Serializer for Credit Card
    """
    id = serializers.CharField()
    name = serializers.CharField()
    number = serializers.CharField()
    close_date = serializers.CharField()
    due_date = serializers.CharField()
    balance_local = serializers.FloatField()
    balance_dollar = serializers.FloatField()


class CreditCardsResponseSerializer(serializers.Serializer):
    """Serializer for User credit cards response
    """
    status = serializers.CharField()
    credit_cards = CreditCardSerializer(many=True)
