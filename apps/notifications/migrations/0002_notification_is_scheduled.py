# Generated by Django 5.2 on 2025-04-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="is_scheduled",
            field=models.BooleanField(default=False),
        ),
    ]
