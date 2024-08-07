# Generated by Django 5.0.6 on 2024-07-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estates', '0014_uservisit'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservisit',
            name='ip_address',
            field=models.GenericIPAddressField(default='0.0.0.0'),
        ),
        migrations.AddField(
            model_name='uservisit',
            name='location',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
