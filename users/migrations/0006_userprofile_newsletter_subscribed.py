# Generated by Django 5.1.2 on 2024-11-07 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='newsletter_subscribed',
            field=models.BooleanField(default=False),
        ),
    ]
