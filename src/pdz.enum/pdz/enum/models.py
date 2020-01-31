from django.utils.translation import gettext as _
from django.db import models

from pdz.base.models import BasicModel



class Service(BasicModel):
    cost = models.DecimalField(verbose_name="Costo", max_digits=6, decimal_places=2)
    
    class Meta:
        verbose_name = _("Trattamento")
        verbose_name_plural = _("Trattamenti")
        ordering = ('title',)
        
# 
# class Country(BasicModel):
#     code = models.CharField(max_length=10)
# 
#     class Meta:
#         verbose_name = _("Nazione")
#         verbose_name_plural = _("Nazioni")
#         ordering = ("title",)
# 
# 
# 
# class SchoolRanking(BasicModel):
# 
#     class Meta:
#         verbose_name = _("Grado d'istruzione")
#         verbose_name_plural = _("Gradi istruzione")
#         ordering = ("title",)
# 
# 
# class MaritalStatus(BasicModel):
# 
#     class Meta:
#         verbose_name = _("Stato civile")
#         verbose_name_plural = _("Stati civili")
#         ordering = ("title",)
# 
# class Job(BasicModel):
# 
#     class Meta:
#         verbose_name = _("Occupazione")
#         verbose_name_plural = _("Occupazioni")
#         ordering = ("title",)
# 
# 
# class CaseType(BasicModel):
# 
#     class Meta:
#         verbose_name = _("Tipologia caso")
#         verbose_name_plural = _("Tipologie caso")
#         ordering = ("title",)
# 
# 
# class UnionType(BasicModel):
# 
#     class Meta:
#         verbose_name = _("Tipo di matrimonio")
#         verbose_name_plural = _("Tipi di matrimonio")
#         ordering = ("title",)
#        
#         
# class FirstAction(BasicModel):
# 
#     class Meta:
#         verbose_name = _("Intervento")
#         verbose_name_plural = _("Interventi")
#         ordering = ("title",)
# 
# 
