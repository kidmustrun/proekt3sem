from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    id_ad = models.AutoField(primary_key=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField('Название объявления', max_length=50)
    description = models.TextField('Описание объявления')
    price = models.IntegerField('Цена')
    geo = models.TextField('Местоположение')
    date = models.DateField('Дата публикации', auto_now_add=True)
    status = models.BooleanField('Продано', default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


