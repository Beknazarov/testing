# coding=utf-8
from django.contrib import admin
from .models import *

# Register your models here.


class ManyChoiceAnswerInline(admin.StackedInline):
    model = ManyChoiceAnswer
    extra = 1


class TrueFalseAnswerInline(admin.StackedInline):
    model = TrueFalseAnswer
    extra = 1


class CompositionAnswerInline(admin.StackedInline):
    model = CompositionAnswer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question
    inlines = [ManyChoiceAnswerInline, TrueFalseAnswerInline,CompositionAnswerInline]


admin.site.register(Question,QuestionAdmin)
