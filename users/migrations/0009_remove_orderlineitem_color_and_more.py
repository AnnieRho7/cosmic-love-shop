# Generated by Django 5.1.2 on 2024-11-09 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_order_country_alter_order_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='color',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='gemstone',
        ),
    ]
