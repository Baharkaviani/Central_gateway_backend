# Generated by Django 4.2.6 on 2023-10-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("board_id", models.CharField(max_length=64)),
                (
                    "data_type",
                    models.CharField(
                        choices=[
                            ("w", "Water"),
                            ("g", "Gas"),
                            ("p", "Power"),
                            ("b", "Battery"),
                        ],
                        max_length=1,
                    ),
                ),
                ("consumption", models.PositiveIntegerField()),
                ("time", models.DateTimeField()),
            ],
            options={
                "db_table": "consumption_data_record",
                "ordering": ["time"],
            },
        ),
    ]
