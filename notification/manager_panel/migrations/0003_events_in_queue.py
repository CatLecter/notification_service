# Generated by Django 4.0.4 on 2022-05-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager_panel", "0002_remove_messagetemplate_file_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="events",
            name="in_queue",
            field=models.BooleanField(
                default=False, verbose_name="Отправлено в очередь?"
            ),
        ),
    ]