# Generated by Django 2.2.5 on 2021-01-23 14:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0017_auto_20210123_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='converstation', to=settings.AUTH_USER_MODEL),
        ),
    ]
