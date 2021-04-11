# Generated by Django 2.2.5 on 2021-01-23 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("conversations", "0007_auto_20210123_2319"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="conversation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="conversations.Conversation",
            ),
        ),
    ]
