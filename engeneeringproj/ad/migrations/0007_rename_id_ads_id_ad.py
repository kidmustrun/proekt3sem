# Generated by Django 3.2.3 on 2021-06-14 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0006_rename_id_ad_ads_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='id',
            new_name='id_ad',
        ),
    ]
