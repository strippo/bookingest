# coding: utf-8
from decimal import Decimal

from pdz.base.models import BasicModel
from django.db import models
from pdz.events.models import Event
from django.utils.translation import ugettext as _
from django.template.defaultfilters import truncatewords


class Appointment(Event):
    DEFAULT_APPOINTMENT_COLOR = '#FF0000'

    operator = models.ForeignKey("workers.Operator", verbose_name=_("Operatrice"), related_name="appointments")
    user = models.ForeignKey("users.User", verbose_name=_("Cliente"))
    service = models.ForeignKey("enum.Service", verbose_name=_("Trattamento"),)
    cost = models.DecimalField(verbose_name="Prezzo", max_digits=6, decimal_places=2)
    total_minutes = models.IntegerField(verbose_name="Minuti", editable=False)
    canceled = models.BooleanField(verbose_name="Cancellato", default= False)


    class Meta:
        verbose_name = _("Trattamento")
        verbose_name_plural = _("Trattamenti")
        ordering = ('-created',)
        permissions = (("can_view_calendar", "Can view calendar"),)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        start = self.start
        end = self.end
        self.total_minutes = (end - start).total_seconds()/60.0
        if self.canceled:
            self.cost = Decimal(0.00)
        super(Appointment, self).save(force_insert, force_update, using, update_fields)

    @property
    def description_html(self):
        description = u"<strong>Operatrice:</strong><br>%s" % self.operator
        description += u"<br/>"
        description += u"<strong>Cliente:</strong><br>%s" %self.user.fullname
        description += u"<br/>"
        description += u"<strong>Trattamento:</strong><br>%s" % self.service

        if self.description:
            description += u"<hr/>" + self.description
        return description

    def to_dict(self, **kwargs):
        color = self.operator.color or self.DEFAULT_APPOINTMENT_COLOR
        full_title = "<p style='text-align:center'><strong>%s</strong><br></p>" % self.operator
        full_title += "<p><strong>%s</strong></p>" % self.user.fullname
        full_title += "<p><strong>%s</strong></p>" % self.service
        return super(Appointment, self).to_dict(color=color, description=self.description_html,
                                                title=full_title, **kwargs)

    @property
    def _title(self):
        time = " (%s %s-%s)" % (
            self.start.strftime("%d/%m/%Y"), self.start.strftime("%H:%M"), self.end.strftime("%H:%M")
        )
        title = self.title or truncatewords(self.description, 5)
        title += time
        return title

    def __unicode__(self):
        return self.service.title

    @models.permalink
    def get_absolute_url(self):
        return ('admin:appointments_appointment_view', (), {'pk': self.pk})
