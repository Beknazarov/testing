# coding=utf-8
from redactor.fields import RedactorField
from django.db import models
from exam.models import Test
from django.utils.text import slugify


def image_upload_to(instance, filename):
    title = instance.title
    slug = slugify(title)
    new_filename = "%s-%s.%s" % (slug, instance.id, filename)
    return "author/%s/%s" % (slug, new_filename)


class Question(models.Model):
    choices = (
        ('Many', 'Many'),
        ('TrueFalse', 'TrueFalse'),
        ('SelfAnswer', 'SelfAnswer'),
        ('Esse', 'Esse'),
    )
    text = models.TextField(verbose_name='Текст', null=True,blank=True)
    test = models.ForeignKey(Test)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)
    point = models.IntegerField()
    answer_type = models.CharField(choices=choices, max_length=20, null=True)

    def __unicode__(self):
        return self.test.title


class ManyChoiceAnswer(models.Model):
    text = models.TextField(verbose_name='Текст', null=True,blank=True)
    right = models.BooleanField()
    question = models.ForeignKey(Question)

class OneChoiceAnswer(models.Model):
    text = models.TextField(verbose_name='Текст', null=True,blank=True)
    right = models.BooleanField()
    question = models.ForeignKey(Question)


class TrueFalseAnswer(models.Model):
    true = models.BooleanField(default=False)
    false = models.BooleanField()
    question = models.ForeignKey(Question)


class CompositionAnswer(models.Model):
    text = RedactorField(
        upload_to=image_upload_to,
        allow_file_upload=True,
        allow_image_upload=True,
        verbose_name='Текст')
    question = models.ForeignKey(Question)
