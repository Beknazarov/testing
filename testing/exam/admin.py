# coding=utf-8
from django.contrib import admin
from .models import Test,Category
# Register your models here.


class TestAdmin(admin.ModelAdmin):
    class Meta:
        model = Test
    list_display = '__unicode__ category'.split()

admin.site.register(Test,TestAdmin)
admin.site.register(Category)
