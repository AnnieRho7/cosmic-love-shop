# Generated by Django 5.1.2 on 2024-11-09 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_orderlineitem_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('RECEIVED', 'Order Received'), ('PROCESSING', 'Processing'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered')], default='RECEIVED', max_length=20, verbose_name='Order Status'),
        ),
    ]
