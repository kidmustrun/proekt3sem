from django.db import models

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
