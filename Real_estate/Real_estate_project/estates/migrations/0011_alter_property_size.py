# Generated by Django 4.2.7 on 2024-04-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estates', '0010_property_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='size',
            field=models.CharField(max_length=300),
        ),
    ]
