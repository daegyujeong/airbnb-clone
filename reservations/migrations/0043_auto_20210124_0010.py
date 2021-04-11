# Generated by Django 2.2.5 on 2021-01-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0042_auto_20210123_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('cancled', 'Cancled'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]
