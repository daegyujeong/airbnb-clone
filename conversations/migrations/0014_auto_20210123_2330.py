# Generated by Django 2.2.5 on 2021-01-23 14:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0013_auto_20210123_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(null=True, related_name='converstation', to=settings.AUTH_USER_MODEL),
        ),
    ]