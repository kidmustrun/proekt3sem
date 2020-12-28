# Generated by Django 3.1.4 on 2020-12-28 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0002_auto_20201228_2033'),
        ('main', '0006_auto_20201228_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Название блога')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.users')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
