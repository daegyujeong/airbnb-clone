# Generated by Django 2.2.5 on 2021-01-20 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Accurancy',
            new_name='accurancy',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Check_in',
            new_name='check_in',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Cleanliness',
            new_name='cleanliness',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Communication',
            new_name='communication',
        ),
    ]
