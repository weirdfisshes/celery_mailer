# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ClientGroup(models.Model):
    name = models.CharField(
        'Название группы',
        max_length=100,
    )
    description = models.CharField(
        'Описание группы',
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа рассылки'
        verbose_name_plural = 'Группы рассылок'

class Client(models.Model):
    name = models.CharField(
        'Имя',
        max_length=100,
    )
    surname = models.CharField(
        'Фамилия',
        max_length=100,
    )
    date_of_birth = models.DateField(
        'Дата рождения',
    )
    email = models.EmailField(
        'Email',
        unique=True,
        null=True
    )
    group = models.ForeignKey(
        ClientGroup,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='clients',
        verbose_name='Группа'
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class MailTemplate(models.Model):
    group = models.ForeignKey(
        ClientGroup,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='mails',
        verbose_name='Группа'
    )
    subject = models.TextField(
        'Тема',
        max_length=150
    )
    body = models.TextField(
        'Тело письма',
        max_length=1000
    )
    mail_from = models.EmailField(
        'Адрес отправителя',
        unique=True,
        null=True,
        default='1@ya.ru'
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Шаблон письма'
        verbose_name_plural = 'Шаблоны писем'

class Mailing(models.Model):
    start_date = models.DateTimeField(verbose_name='Начало рассылки')
    mail_template = models.ForeignKey(
        MailTemplate,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='mailings',
        verbose_name='Письмо'
    )
    group = models.ForeignKey(
        ClientGroup,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='mailings',
        verbose_name='Группа'
    )

    def __str__(self):
        return self.group.name

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

class ClientMail(models.Model):
    READ = 'read'
    NOT_READ = 'not read'
    STATUS_CHOICES = [
        (READ, 'Прочитано'),
        # (NOT_READ, 'Не прочитано'),
    ]
    client = models.ForeignKey(
        Client,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='client_mails',
        verbose_name='Клиент'
    )
    mail_template = models.ForeignKey(
        MailTemplate,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='client_mails',
        verbose_name='Шаблон письма'
    )
    mailing = models.ForeignKey(
        Mailing,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='client_mails',
        verbose_name='Рассылка'
    )
    status = models.CharField(
        verbose_name='Статус письма',
        max_length=20,
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = 'Письмо клиента'
        verbose_name_plural = 'Письма клиентов'
