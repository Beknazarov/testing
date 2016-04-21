from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import MyUser
from .forms import UserChangeForm, UserCreationForm
from .widgets import AdvancedFileInput
from django.db import models


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('avatar_pic', 'email', 'username', 'is_admin', 'is_active', 'date_joined')
    list_filter = ('is_admin', 'is_teacher', 'is_student')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'avatar', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_student', 'is_teacher')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()
    formfield_overrides = {models.ImageField: {'widget': AdvancedFileInput}}


admin.site.register(MyUser, UserAdmin)

# unregister the Group model from admin.
admin.site.unregister(Group)
