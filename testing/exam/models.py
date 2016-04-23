# coding=utf-8
from django.db import models
from django.template.defaultfilters import date
from django.utils.text import slugify
from redactor.fields import RedactorField
from django.conf import settings


def image_upload_to(instance, filename):
    title = instance.title
    slug = slugify(title)
    new_filename = "%s-%s.%s" % (slug, instance.id, filename)
    return "author/%s/%s" % (slug, new_filename)

# Create your models here.


class Test(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    instruction = models.TextField(null=True, blank = True)
    category = models.ForeignKey('Category', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

    def __unicode__(self):
        return self.title

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
