# Generated by Django 5.1.6 on 2025-03-19 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_remove_task_lenght_alter_task_date_of_create_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date_of_create',
            new_name='date_of_start',
        ),
    ]
