import datetime

from django.db import models

# Create your models here.
class Block(models.Model):
    block_id = models.IntegerField(verbose_name='Высота блока', unique=True, primary_key=True)
    block_hash = models.CharField(verbose_name='Хэш блока', max_length=64, unique=True)
    block_time = models.DateTimeField(verbose_name='Время блока', auto_now_add=True)
    miner_address = models.CharField(verbose_name='Адрес майнера', max_length=128, unique=True)
    num_trans_in_block = models.IntegerField(verbose_name='Количество транзакций в блоке')

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'





