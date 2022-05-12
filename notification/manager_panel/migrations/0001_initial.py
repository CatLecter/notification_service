# Generated by Django 4.0.4 on 2022-05-12 18:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания события')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления события')),
                ('notification_id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, verbose_name='id события')),
                ('last_notification_send', models.DateTimeField(default=None, null=True, verbose_name='Дата отправки уведомления')),
                ('source', models.CharField(choices=[('UGC', 'UGC'), ('AUTH', 'AUTH'), ('USER', 'USER'), ('ADMIN', 'ADMIN')], max_length=20, verbose_name='Сервис-источник')),
                ('event_type', models.CharField(choices=[('URGENT', 'URGENT'), ('REGULAR', 'REGULAR')], max_length=20, verbose_name='Приоритет')),
                ('content_id', models.UUIDField(verbose_name='UUID сущности')),
                ('action', models.CharField(choices=[('DELETE', 'DELETE'), ('CREATE', 'CREATE'), ('UPDATE', 'UPDATE'), ('ADD', 'ADD'), ('LOGIN', 'LOGIN'), ('REGISTRATION', 'REGISTRATION')], max_length=20, verbose_name='Действие')),
                ('data_endpoint', models.URLField(blank=True, verbose_name='Эндпоинт получения данных о сущности')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'db_table': '"public"."events"',
            },
        ),
        migrations.CreateModel(
            name='MessageTemplate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания события')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления события')),
                ('name', models.CharField(max_length=255, verbose_name='Имя элемента шаблона')),
                ('template_type', models.CharField(choices=[('header', 'HEADER'), ('body', 'BODY'), ('footer', 'FOOTER')], max_length=20, verbose_name='Тип элемента шаблона')),
                ('file', models.FileField(blank=True, upload_to='templates')),
            ],
            options={
                'verbose_name': 'Шаблон сообщения',
                'verbose_name_plural': 'Шаблоны сообщения',
                'db_table': '"public"."message_templates"',
            },
        ),
    ]
