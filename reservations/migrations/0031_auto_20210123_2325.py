# Generated by Django 2.2.5 on 2021-01-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0030_auto_20210123_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('cancled', 'Cancled'), ('pending', 'Pending'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]
