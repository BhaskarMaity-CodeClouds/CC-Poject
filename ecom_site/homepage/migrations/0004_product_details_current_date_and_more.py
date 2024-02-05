# Generated by Django 5.0 on 2024-01-30 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_product_details_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='current_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
