# Generated by Django 2.2.5 on 2021-01-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_auto_20210119_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('cancled', 'Cancled'), ('pending', 'Pending'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]
