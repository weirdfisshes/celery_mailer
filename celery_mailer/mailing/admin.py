# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    ClientGroup, Client, MailTemplate,
    Mailing, ClientMail
)


@admin.register(ClientGroup)
class ClientGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    empty_value_display = '-empty-'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'date_of_birth', 'email', 'group')
    empty_value_display = '-empty-'


@admin.register(MailTemplate)
class MailTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'subject', 'html_template', 'mail_from')
    empty_value_display = '-empty-'


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'mail_template', 'group')
    empty_value_display = '-empty-'


@admin.register(ClientMail)
class ClientMailAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'mail_template', 'mailing', 'status')
    empty_value_display = '-empty-'