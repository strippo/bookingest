# -*- coding: utf-8 -*-
from pdz.base.models import Person, BasicModel
from pdz.base.models.mixins import CodeModelMixin
from django.db import models
from django.utils.translation import gettext as _
from protected_filefield.fields import ProtectedFileField
from protected_filefield.settings import PRIVATE_ROOT


class User(Person):
    active = models.BooleanField(verbose_name=_("Attivo"), default=True)
#    is_active = models.BooleanField(verbose_name=_("Attivo"))
#    gender = models.PositiveIntegerField(verbose_name=_("Sesso"), choices=SEX_CHOICES, null=True, blank=False)
    birth_date = models.DateField(verbose_name=_("Data di nascita"), null=True, blank=True)
#    birth_place = models.CharField(max_length=50, verbose_name=_("Luogo di nascita"), null=True, blank=True)
#    school_ranking = models.ForeignKey("enum.SchoolRanking", verbose_name="Grado d'istruzione",
#                                       null=True, blank=True, on_delete=models.SET_NULL)
#    job = models.ForeignKey("enum.Job", verbose_name="Occupazione", null=True, blank=True,
#                            on_delete=models.SET_NULL)
#    marital_status = models.ForeignKey("enum.MaritalStatus", verbose_name="Stato civile", null=True, blank=True,
#                                       on_delete=models.SET_NULL)
#    union_type = models.ForeignKey("enum.UnionType", verbose_name="Tipo di matrimonio", null=True, blank=True,
#                                    on_delete=models.SET_NULL)
#    relation_duration = models.CharField(max_length=70, verbose_name=_("Durata relazione attuale"), null=True, blank=True)
#    sons_number = models.CharField(max_length=25, verbose_name=_("Numero figli"), null=True, blank=True)
#    family_number = models.CharField(max_length=25, verbose_name=_("Numero componenti familiari"), null=True, blank=True)
#     request_recipient = models.CharField(max_length=25, verbose_name=_("Per chi fa richiesta"), null=True, blank=True)
#     source = models.CharField(max_length=25, verbose_name=_("Inviante"), null=True, blank=True)
#     case_type = models.ForeignKey("enum.CaseType", verbose_name="Tipologia caso", null=True, blank=True)
#     first_aid = models.CharField(max_length=255, verbose_name=_("Primo Intervento"), null=True, blank=True)
#     first_action = models.ForeignKey("enum.FirstAction", verbose_name=_("Primo Intervento"), null=True, blank=True)
#     availabilities = models.TextField(verbose_name=_("Giorni e orari disponibili"), null=True, blank=True)
#     group_therapy = models.BooleanField(verbose_name="Disponibilità a terapia di gruppo")
#     possible_requests = models.TextField(verbose_name=_("Eventuali richieste"), null=True, blank=True)
#     # observations = models.TextField(verbose_name=_("Osservazioni"), null=True, blank=True)
#     checkin_card = models.FileField(verbose_name=_("Scheda privacy"), null=True, blank=True,
#                                                     upload_to=lambda self, p: "%s%s%s%s" % (PRIVATE_ROOT,
#                                                                                             "users/checkin",
#                                                                                           self.pk, p))

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clienti')
        ordering = ('surname', 'name')

    @models.permalink
    def get_absolute_url(self):
        return ("admin:users_user_view", (), {"pk":self.pk})


def get_user_attachment_path(self, filename):
    return "user/%s/attachments/%s" % (self.user.pk, filename)

class UserAttachment(BasicModel):
    UPLOAD_TO = 'users_files'
    user = models.ForeignKey("users.User", related_name='user_files')
    attachment = ProtectedFileField(verbose_name=_("Allegato"),
                                    null=True,
                                    blank=True,
                                    upload_to=get_user_attachment_path)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Allegato')
        verbose_name_plural = _('Allegati')