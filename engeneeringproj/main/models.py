from django.db import models

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Jobs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Название вакансии', max_length=50)
    text = models.TextField('Описание')
    salary = models.IntegerField('Заработная плата')
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


