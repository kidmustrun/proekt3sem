from django.db import models


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    password = models.CharField('Пароль', max_length=50)
    phone = models.CharField('Телефон', max_length=20)
    email = models.CharField('Email', max_length=50)
    role = models.CharField('Роль', max_length=20)
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.IntegerField('ID пользователя')
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



class Credit(models.Model):
    id_credit = models.ForeignKey('Ads', on_delete=models.CASCADE)
    percent = models.DecimalField('Процент под ипотеку', max_digits=5, decimal_places=3)
    class Meta:
        verbose_name = "Условие ипотеки"
        verbose_name_plural = "Условия ипотеки"
