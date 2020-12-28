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
class Documents(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField('Название документа')
    url = models.URLField('Ссылка на документ')
    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('ad.Users', on_delete=models.CASCADE)
    title = models.CharField('Название блога', max_length=50)
    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    id_blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    title = models.CharField('Название статьи', max_length=50)
    text = models.TextField('Текст статьи')
    date = models.DateField('Дата публикации')
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
