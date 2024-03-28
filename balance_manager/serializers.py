from balance_manager.models import Consumer, Balance
from rest_framework import serializers


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['id', 'reference_no', 'amount', 'status', 'created_at']


class ConsumerSerializer(serializers.ModelSerializer):
    balances = BalanceSerializer(many=True, read_only=True)

    class Meta:
        model = Consumer
        fields = ['id', 'name', 'ssn', 'agency', 'balances']
