# Generated by Django 3.2.3 on 2021-07-12 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_requestticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestticket',
            name='user',
        ),
    ]
