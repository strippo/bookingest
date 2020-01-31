from django.db import models
from django.utils.translation import ugettext as _


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Data creazione"), null=True)
    modified = models.DateTimeField(auto_now=True, verbose_name=_("Data modifica"), null=True)

    #    def get_file_destination(instance, filename):
    #        cls_name = instance.__class__.__name__.lower()
    #        return '%s/%s/%s' % (cls_name, instance.pk, filename)
    class Meta:
        abstract = True


class BasicModel(BaseModel):
    title = models.CharField(verbose_name=_("Denominazione"), max_length=255)
    description = models.TextField(verbose_name=_("Descrizione"), blank=True)

    def __unicode__(self):
        return "%s" % self.title

    class Meta:
        abstract = True

    @models.permalink
    def get_absolute_url(self):
        return ("admin:%s_%s_%s" % (self._meta.app_label,
                                    self.__class__.__name__.lower(),
                                    "view"), (),
                {'pk': self.pk})
