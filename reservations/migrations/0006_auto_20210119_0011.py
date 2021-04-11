# Generated by Django 2.2.5 on 2021-01-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20210119_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('cancled', 'Cancled'), ('pending', 'Pending')], default='pending', max_length=12),
        ),
    ]
