# Generated by Django 4.2 on 2024-01-22 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_remove_orderitem_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="pay_day",
            field=models.DateTimeField(null=True),
        ),
    ]
