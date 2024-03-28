from django.test import TestCase
from django.urls import reverse
from balance_manager.models import Agency, Consumer, Balance

from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework import status


# Create your tests here.

class ConsumerApiTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = '/consumers/'
        agency = Agency.objects.create(name="Test Agency")
        self.sequence = [1, 2, 3, 4, 5]

        for num in self.sequence:
            ssn = f"ssn-{num}"
            name = f"test-user-{num}"
            address = f"test address {num}"
            reference_no = f"reference-{num}"
            status = "INACTIVE"

            consumer = Consumer.objects.create_consumer(name, ssn, address, agency)
            Balance.objects.create(amount=float(num), status=status, reference_no=reference_no, consumer=consumer)

    def make_consumer_request(self, data):
        response = self.client.get(self.url, data=data, format='json')
        return response.data['consumers']

    def test_get_consumers_with_inactive_status(self):
        consumers = self.make_consumer_request({'status': 'inactive'})
        self.assertEqual(len(consumers), len(self.sequence))

    def test_get_consumers_with_wrong_status(self):
        consumers = self.make_consumer_request({'status': 'unknown'})
        self.assertEqual(len(consumers), 0)

    def test_get_consumers_with_name(self):
        consumers = self.make_consumer_request({'consumer_name': 'test-user-1'})
        self.assertEqual(len(consumers), 1)

    def test_get_consumers_with_min_balance(self):
        consumers = self.make_consumer_request({'min_balance': 5})
        self.assertEqual(len(consumers), 1)

    def test_get_consumers_with_max_balance(self):
        consumers = self.make_consumer_request({'max_balance': 5})
        self.assertEqual(len(consumers), 5)

    def test_get_consumers_with_min_and_max_balance(self):
        consumers = self.make_consumer_request({'max_balance': 5, 'min_balance': 4})
        self.assertEqual(len(consumers), 2)
