# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = (
        'fio',
        'group_number',
        'test_number',
        'wrong_answers',
        'mark',
        'date'
    )


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'part')
    inlines = [AnswerInline]
