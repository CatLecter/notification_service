# Generated by Django 4.0.4 on 2022-05-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager_panel", "0003_events_in_queue"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="source",
            field=models.CharField(
                choices=[
                    ("", "UGC"),
                    ("AUTH", "AUTH"),
                    ("USER", "USER"),
                    ("ADMIN", "ADMIN"),
                ],
                max_length=20,
                verbose_name="Сервис-источник",
            ),
        ),
    ]