# Generated by Django 5.1.7 on 2025-03-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("way_bills_creator", "0002_event_event_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event_id",
            field=models.PositiveIntegerField(verbose_name="id из TeamUp"),
        ),
    ]
