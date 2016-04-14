# coding=utf-8
from redactor.fields import RedactorField
from django.db import models
from exam.models import Test
from django.utils.text import slugify


def image_upload_to(instance, filename):
    title = instance.title
    slug = slugify(title)
    new_filename = "%s-%s.%s" % (slug, instance.id, file_extension)
    return "author/%s/%s" % (slug, new_filename)


class Question(models.Model):
    choices = (
        ('Many', 'Many'),
        ('TrueFalse', 'TrueFalse'),
        ('SelfAnswer', 'SelfAnswer'),
        ('Esse', 'Esse'),
    )
    text = RedactorField(
        allow_file_upload=True,
        allow_image_upload=True,
        verbose_name='Текст')
    test = models.ForeignKey(Test)
    point = models.IntegerField()
    answer_type = models.CharField(choices=choices, max_length=20, null=True)

    def __unicode__(self):
        return self.test.title


class ManyChoiceAnswer(models.Model):
    variation = models.CharField(max_length=100, null=True, blank=True)
    text = RedactorField(
        upload_to=image_upload_to,
        allow_file_upload=True,
        allow_image_upload=True,
        verbose_name='Текст')
    right = models.BooleanField()
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.variation

    def save(self, *args, **kwargs):
        answers = ManyChoiceAnswer.objects.filter(question=self.question)
        if self.variation.__len__() > 0:
            super(ManyChoiceAnswer, self).save(*args, **kwargs)
        else:
            count = answers.count()
            self.variation = chr(count + 65)
            super(ManyChoiceAnswer, self).save(*args, **kwargs)


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
