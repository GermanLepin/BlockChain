# Generated by Django 3.1.6 on 2021-02-11 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('block_id', models.IntegerField(max_length=8, primary_key=True, serialize=False, unique=True, verbose_name='Высота блока')),
                ('block_hash', models.CharField(max_length=64, unique=True, verbose_name='Хэш блока')),
                ('block_time', models.DateTimeField(auto_now_add=True, verbose_name='Время блока')),
                ('miner_address', models.CharField(max_length=128, unique=True, verbose_name='Адрес майнера')),
                ('num_trans_in_block', models.IntegerField(max_length=16, verbose_name='Количество транзакций в блоке')),
            ],
            options={
                'verbose_name': 'Блок',
                'verbose_name_plural': 'Блоки',
            },
        ),
    ]
