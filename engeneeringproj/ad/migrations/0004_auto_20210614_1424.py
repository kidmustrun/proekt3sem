# Generated by Django 3.2.3 on 2021-06-14 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0003_auto_20210614_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='id',
        ),
        migrations.AddField(
            model_name='ads',
            name='current_user',
            field=models.ForeignKey(default='user', on_delete=django.db.models.deletion.PROTECT, to='ad.users'),
            preserve_default=False,
        ),
    ]