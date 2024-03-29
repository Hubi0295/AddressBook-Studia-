# Generated by Django 3.2.3 on 2023-05-01 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0004_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='second_name',
        ),
        migrations.AddField(
            model_name='address',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='middle_name',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
