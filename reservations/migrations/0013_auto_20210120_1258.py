# Generated by Django 2.2.5 on 2021-01-20 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0012_auto_20210119_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('cancled', 'Cancled'), ('pending', 'Pending')], default='pending', max_length=12),
        ),
    ]
