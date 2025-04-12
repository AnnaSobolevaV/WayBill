# Generated by Django 5.1.7 on 2025-04-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "way_bills_creator",
            "0005_location_location_name_alter_location_address_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="driver",
            name="lic_date",
            field=models.DateField(blank=True, null=True, verbose_name="дата начала"),
        ),
        migrations.AddField(
            model_name="driver",
            name="lic_num",
            field=models.CharField(
                blank=True,
                max_length=150,
                null=True,
                verbose_name="Номер водительских прав",
            ),
        ),
        migrations.AddField(
            model_name="driver",
            name="snils_num",
            field=models.CharField(
                blank=True, max_length=150, null=True, verbose_name="СНИЛС водителя"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="дата окончания"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateField(blank=True, null=True, verbose_name="дата начала"),
        ),
    ]
