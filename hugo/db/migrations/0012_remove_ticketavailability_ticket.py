# Generated by Django 3.2.3 on 2021-07-12 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_ticketavailability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketavailability',
            name='ticket',
        ),
    ]
