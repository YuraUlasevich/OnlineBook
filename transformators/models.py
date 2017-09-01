# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    text = models.TextField(verbose_name=u'Текст вопроса')
    part = models.IntegerField(verbose_name=u'Принадлежность к тесту №')

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name=u'Вопрос')
    name = models.CharField(max_length=100, verbose_name=u'Имя переменной')
    answer = models.CharField(max_length=100, verbose_name=u'Ответ')

    class Meta:
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'


class Pupil(models.Model):
    fio = models.CharField(max_length=200, verbose_name=u'ФИО ученика')
    group_number = models.CharField(max_length=100, verbose_name=u'Номер группы')
    test_number = models.IntegerField(verbose_name=u'Номер теста', null=True)
    mark = models.IntegerField(verbose_name=u'Оценка', null=True)
    wrong_answers = models.TextField(verbose_name=u'Неправильные ответы')
    date = models.DateTimeField(auto_now=True, verbose_name=u'Дата и время начала')
 
    class Meta:
        verbose_name = u'Результат'
        verbose_name_plural = u'Результаты'
