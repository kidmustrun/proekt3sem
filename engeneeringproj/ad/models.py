from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    id_ad = models.AutoField(primary_key=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField('Название объявления', max_length=50)
    description = models.TextField('Описание объявления')
    price = models.IntegerField('Цена')
    geo = models.TextField('Местоположение')
    date = models.DateField('Дата публикации')
    status = models.BooleanField('Продано')
    id_credit = models.IntegerField('ID условий ипотеки')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

class Credit(models.Model):
    id_credit = models.ForeignKey('Ad', on_delete=models.CASCADE)
    percent = models.DecimalField('Процент под ипотеку', max_digits=5, decimal_places=3)

    class Meta:
        verbose_name = "Условие ипотеки"
        verbose_name_plural = "Условия ипотеки"

