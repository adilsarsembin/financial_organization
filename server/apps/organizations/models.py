from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class FinancialOrganization(models.Model):
    director_board_chairman = models.ForeignKey(
        verbose_name=_('Председатель Совета директоров'),
        to=User,
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )
    management_board_chairman = models.ForeignKey(
        verbose_name=_('Председатель Правления'),
        to=User,
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )
    directors_board = models.ManyToManyField(
        verbose_name=_('Совет директоров'),
        to=User,
        related_name='+',
        blank=True,
    )
    management_board_members = models.ManyToManyField(
        verbose_name=_('Члены Правления'),
        to=User,
        related_name='+',
        blank=True,
    )
    chief_accountant = models.ForeignKey(
        verbose_name=_('Председатель Совета директоров'),
        to=User,
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )
    bin = models.CharField(verbose_name=_('БИН'), max_length=12)
    address = models.CharField(
        verbose_name=_('Адрес'),
        max_length=512,
        help_text=_('Город, улица, дом, квартира'),
        blank=True,
    )
    phone_number = PhoneNumberField(verbose_name=_('Телефон'), blank=True)
    fax = PhoneNumberField(verbose_name=_('Факс'), blank=True)
    email = models.EmailField(verbose_name=_('E-mail'), blank=True)
    url = models.URLField(verbose_name=_('Web-сайт'), blank=True)
    license = models.CharField(
        verbose_name=_('Лицензия'), max_length=512, blank=True
    )

    def __str__(self):
        return f'Финансовая организация {self.bin}'


class FinancialOrganizationNews(models.Model):
    content = models.TextField(_('Контент'))
    financial_organization = models.ForeignKey(
        verbose_name=_('Финансовая организация'),
        to=FinancialOrganization,
        on_delete=models.CASCADE,
        related_name='news',
    )

    def __str__(self):
        return f'Новость {self.financial_organization}'
