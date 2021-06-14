from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='категория')

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(verbose_name='вопрос')
    answer = models.TextField(verbose_name='ответ', blank=True)
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='категория',
        related_name='questions',
    )

    def __str__(self):
        return self.question
