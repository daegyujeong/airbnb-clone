# Generated by Django 2.2.5 on 2021-01-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0018_auto_20210123_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
