# Generated by Django 5.1.7 on 2025-03-31 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("way_bills_creator", "0003_alter_event_event_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event_id",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="id из TeamUp"
            ),
        ),
    ]
