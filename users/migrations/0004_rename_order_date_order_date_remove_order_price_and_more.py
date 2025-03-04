# Generated by Django 5.1.2 on 2024-10-31 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image'),
        ('users', '0003_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default='Unknown', max_length=40),
        ),
        migrations.AddField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='unknown@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(default='Guest', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='grand_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='ORD0000', editable=False, max_length=32),
        ),
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='street_address1',
            field=models.CharField(default='Default Street Address', max_length=80),
        ),
        migrations.AddField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, default='Default Street Address', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(default='Default Street Address', max_length=40),
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('gemstone', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='users.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
