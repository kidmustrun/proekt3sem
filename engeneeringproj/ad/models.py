from django.db import models
class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    id_author = models.IntegerField('ID автора')
    title = models.CharField('Название объявления', max_length=50)
    description = models.TextField('Описание объявления')
    price = models.IntegerField('Цена')
    geo = models.TextField('Местоположение')
    date = models.DateField('Дата публикации')
    status = models.BooleanField('Продано')
    id_credit = models.IntegerField('ID условий ипотеки')
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

