# Generated by Django 3.2.3 on 2023-05-01 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0002_auto_20230501_1943'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Voivodeship',
        ),
        migrations.AlterModelOptions(
            name='voivodeship',
            options={'ordering': ('name',), 'verbose_name_plural': 'Voivodeships'},
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
