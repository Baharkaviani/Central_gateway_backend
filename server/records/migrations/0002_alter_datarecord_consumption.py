# Generated by Django 4.2.6 on 2023-10-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("records", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datarecord",
            name="consumption",
            field=models.FloatField(),
        ),
    ]
