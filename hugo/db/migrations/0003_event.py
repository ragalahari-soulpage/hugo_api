# Generated by Django 3.2.3 on 2021-06-23 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20210623_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.FileField(blank=True, default='hugo_users/upcoming-events-icon.svg', upload_to='hugo_users/')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'db_table': 'events',
            },
        ),
    ]
