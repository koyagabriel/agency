# Generated by Django 5.0.3 on 2024-03-27 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("balance_manager", "0002_alter_consumer_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="consumer", unique_together={("name", "ssn")},
        ),
    ]
