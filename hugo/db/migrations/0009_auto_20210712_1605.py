# Generated by Django 3.2.3 on 2021-07-12 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_remove_requestticket_approval_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestticket',
            name='ticket',
        ),
        migrations.AddField(
            model_name='requestticket',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='db.user'),
            preserve_default=False,
        ),
    ]