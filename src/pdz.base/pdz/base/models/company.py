from django.contrib.localflavor.it.it_province import PROVINCE_CHOICES
from django.db import models
# from django_localflavor_it.it_province import PROVINCE_CHOICES

from pdz.base.models import base

class Company(base.BaseModel):
    name = models.CharField(max_length=75)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    cap = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=2, choices=PROVINCE_CHOICES, blank=True)
    country = models.ForeignKey('enum.Nazione', blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True)
    fax = models.CharField(max_length=25, blank=True)
    email = models.EmailField(blank=True)
    vat_number = models.CharField(max_length=11, blank=True)
    tax_code = models.CharField(max_length=16, blank=True)

    __unicode__ = lambda self: u'%s' % self.ragione_sociale

    class Meta:
        abstract = True
