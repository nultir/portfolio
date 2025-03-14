# Generated by Django 5.1.6 on 2025-03-13 20:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_technologies'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologies',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
