# coding:utf-8
from pdz.events.models import Event
from django.db import models
from django.utils.translation import ugettext as _
from pdz.base.models import BaseModel


class Operator(BaseModel):
    code = models.CharField(max_length=10, verbose_name=_("Codice"), blank=True)
    name = models.CharField(max_length=35, verbose_name=_("Nome"))
    surname = models.CharField(max_length=35, verbose_name=_("Cognome"))
    color = models.CharField(max_length=7, verbose_name=_("Colore su calendario appuntamenti"),
                             blank=True, null=True)
    active = models.BooleanField(verbose_name=_("Attivo"), default=True)

    def __unicode__(self):
        return "%s %s" % (self.surname, self.name or '')

    def _fullname(self):
        return self.__unicode__()
    _fullname.short_description = _("Nome completo")
    fullname = property(_fullname)

    class Meta:
        app_label = 'workers'
        verbose_name = _("Operatrice")
        verbose_name_plural = _("Operatrici")
        ordering = ('surname', 'name')

# 
class OperatorAvailability(Event):
#     #expert = models.ForeignKey(Operator, related_name="availabilites")
#     # days = WeekdayField(verbose_name=_("Giorni settimana"))
#     # start = models.TimeField(verbose_name=_("Ora inizio"))
#     # end = models.TimeField(verbose_name=_("Ora fine"))
#     #
    class Meta:
        verbose_name = _(u"Disponibilità")
        verbose_name_plural = _(u"Disponibilità")

# import pdz.workers.signals

