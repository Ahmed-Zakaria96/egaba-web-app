# Generated by Django 3.1.3 on 2021-05-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verified_user',
            field=models.BooleanField(default=False),
        ),
    ]
