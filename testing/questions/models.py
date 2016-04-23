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

    def save(self, *args, **kwargs):
        super(Question, self).save()
        if self.answer_type == 'TrueFalse':
            trueFalseAnswers = TrueFalseAnswer.objects.filter(question_id = self.id)
            if not trueFalseAnswers.count():
                trueFalseAnswer = TrueFalseAnswer.objects.create(question = self)
                trueFalseAnswer.save()
        elif self.answer_type == 'Esse':
            esse = CompositionAnswer.objects.filter(question_id = self.id)
            if not esse.count():
                esse = CompositionAnswer(question_id = self.id)
                esse.save()

class ManyChoiceAnswer(models.Model):
    text = models.CharField(max_length = 500,verbose_name='Текст', null=True,blank=True)
    right = models.BooleanField()
    question = models.ForeignKey(Question)


class TrueFalseAnswer(models.Model):
    true = models.BooleanField(default=False)
    false = models.BooleanField(default = False)
    question = models.ForeignKey(Question)


class CompositionAnswer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question)
