# Generated by Django 2.2.5 on 2021-01-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0011_auto_20210119_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('cancled', 'Cancled'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]