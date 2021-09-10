# Generated by Django 2.2.5 on 2021-01-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0013_auto_20210120_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('cancled', 'Cancled'), ('pending', 'Pending'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]