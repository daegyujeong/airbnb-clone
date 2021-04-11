# Generated by Django 2.2.5 on 2021-01-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0045_auto_20210124_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('cancled', 'Cancled')], default='pending', max_length=12),
        ),
    ]
