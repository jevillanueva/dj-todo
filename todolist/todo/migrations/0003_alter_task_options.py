# Generated by Django 5.0.4 on 2024-04-12 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': [('can_view_tasks', 'Can view tasks')]},
        ),
    ]
