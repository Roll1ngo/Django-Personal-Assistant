# Generated by Django 5.0.4 on 2024-05-08 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="note",
            field=models.CharField(max_length=100000),
        ),
    ]
