# Generated by Django 3.2.3 on 2023-05-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0006_auto_20230518_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voivodeship',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
