from django.db import models


class Quiz(models.Model):
    question = models.TextField(max_length= 3000, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


class Answer(models.Model):
    answer = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Ответ')
    poll = models.ForeignKey('webapp.Quiz', related_name='answer', verbose_name='Вопрос',
                             on_delete=models.CASCADE)