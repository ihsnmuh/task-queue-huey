# Generated by Django 5.2 on 2025-04-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="is_notified",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("completed", "Completed"),
                    ("overdue", "Overdue"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
