# Generated by Django 4.2 on 2024-01-23 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0005_alter_order_pay_day"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="pay_day",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 28, 21, 30, 12, 908259, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]