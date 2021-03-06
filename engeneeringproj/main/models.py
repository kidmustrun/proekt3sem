from django.db import models

class News(models.Model):
    id_new = models.AutoField(primary_key=True)
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Jobs(models.Model):
    id_job = models.AutoField(primary_key=True)
    title = models.CharField('Название вакансии', max_length=50)
    text = models.TextField('Описание')
    salary = models.IntegerField('Заработная плата')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Documents(models.Model):
    id_document = models.AutoField(primary_key=True)
    title = models.TextField('Название документа')
    url = models.URLField('Ссылка на документ')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"


class Blog(models.Model):
    id_blog = models.AutoField(primary_key=True)
    title = models.CharField('Название блога', max_length=50)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"


class Articles(models.Model):
    id_article = models.AutoField(primary_key=True)
    id_blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    title = models.CharField('Название статьи', max_length=50)
    text = models.TextField('Текст статьи')
    date = models.DateField('Дата публикации')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Questions(models.Model):
    id_question = models.AutoField(primary_key=True)
    text = models.TextField('Текст вопроса')
    def __str__(self):
        return self.text
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answers(models.Model):
    id_answer = models.AutoField(primary_key=True)
    id_question = models.ForeignKey('Questions', on_delete=models.CASCADE)
    text = models.TextField('Текст ответа')
    def __str__(self):
        return self.text
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"