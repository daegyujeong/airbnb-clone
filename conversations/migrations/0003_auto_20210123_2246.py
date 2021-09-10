# Generated by Django 2.2.5 on 2021-01-23 13:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conversations", "0002_auto_20210123_2245"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conversation",
            name="participants",
            field=models.ManyToManyField(
                related_name="converstation", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]