# Generated by Django 2.2.5 on 2021-01-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0021_auto_20210123_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
