# Generated by Django 3.2.3 on 2021-07-12 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_remove_requestticket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestticket',
            name='approval_from',
        ),
    ]
