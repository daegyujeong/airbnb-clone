# Generated by Django 2.2.5 on 2021-01-18 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_auto_20210119_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='house_rules',
        ),
    ]
