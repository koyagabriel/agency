from django.shortcuts import get_object_or_404

from balance_manager.models import Consumer
from balance_manager.serializers import ConsumerSerializer

from rest_framework import viewsets
from rest_framework.response import Response


class ConsumerViewSet(viewsets.ViewSet):

    def list(self, request) -> Response:
        queryset = Consumer.objects.all()

        min_balance = request.query_params.get('min_balance')
        if min_balance is not None:
            queryset = queryset.filter(balances__amount__gte=min_balance)

        max_balance = request.query_params.get('max_balance')
        if max_balance is not None:
            queryset = queryset.filter(balances__amount__lte=max_balance)

        consumer_name = request.query_params.get('consumer_name')
        if consumer_name is not None:
            queryset = queryset.filter(name__icontains=consumer_name)

        status = request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(balances__status=status.upper())

        serializer = ConsumerSerializer(queryset.distinct(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Consumer.objects.all()
        consumer = get_object_or_404(queryset, pk=pk)
        serializer = ConsumerSerializer(consumer)
        return Response(serializer.data)
