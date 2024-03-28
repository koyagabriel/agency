import string
from django.db import models
from django.conf import settings


class Agency(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class ConsumerManager(models.Manager):
    def create_consumer(self, name: string, ssn: string, address: string, agency: Agency) -> models.Model:
        consumer = super().get_queryset().filter(name=name, ssn=ssn, agency=agency).first()
        if consumer is None:
            consumer = self.create(name=name, ssn=ssn, address=address, agency=agency)
        return consumer


class Consumer(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    ssn = models.CharField(max_length=20, blank=False, null=False)
    address = models.TextField(null=True)
    agency = models.ForeignKey(Agency, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ConsumerManager()

    class Meta:
        unique_together = ('name', 'ssn')


class Balance(models.Model):
    amount = models.DecimalField(max_digits=19, blank=False, null=False, decimal_places=2)
    status = models.CharField(blank=False, null=True, choices={i: i for i in settings.BALANCE_STATUS})
    reference_no = models.CharField(max_length=100, blank=False, null=False)
    consumer = models.ForeignKey(Consumer, null=False, blank=False, on_delete=models.CASCADE, related_name='balances')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
