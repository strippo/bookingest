# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.localflavor.it.it_province import PROVINCE_CHOICES
from django.utils.translation import ugettext as _

from pdz.base.models import base


class Person(base.BaseModel):
    name = models.CharField(max_length=25, verbose_name=_("Nome"))
    surname = models.CharField(max_length=25, verbose_name=_("Cognome"))
    address = models.CharField(max_length=75, verbose_name=_("Indirizzo"), blank=True)
    city = models.CharField(max_length=50, verbose_name=_("Citta"), blank=True)
    zip_code = models.CharField(max_length=10, verbose_name=_("CAP"), blank=True)
#    province = models.CharField(max_length=2, verbose_name=_("Prov."), null=True, blank=True, choices=PROVINCE_CHOICES)
    phone = models.CharField(max_length=35, verbose_name=_("Telefono"), blank=True)
    mobile = models.CharField(max_length=35, verbose_name=_("Cellulare"), blank=True)
    email = models.EmailField(blank=True, verbose_name=_("E-mail"))
    facebook_account = models.CharField(max_length=40, verbose_name=_("Account Facebook"), blank=True)


    __unicode__ = lambda self: u'%s %s' % (self.surname, self.name)

    class Meta:
        abstract = True

    def _fullname(self):
        return"%s %s" % (self.surname, self.name or '')
    _fullname.short_description = _("Cognome e nome")
    fullname = property(_fullname)

    def _fulladdress(self):
        return"%s %s %s" % (self.address, self.zip_code or '', self.city or '')
    _fulladdress.short_description = _("Indirizzo")
    fulladdress = property(_fullname)

    def colored_is_published(self):
        if self.is_published:
            cell_html = '<span style="color: red;">%s</span>'
        else:
            cell_html = '<span>%s</span>'
        # for below line, you may consider using 'format_html', instead of python's string formatting
        return cell_html % self.is_published
    colored_is_published.allow_tags = True
