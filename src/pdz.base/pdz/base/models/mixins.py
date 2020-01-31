from django.db import models
from django.utils.translation import gettext as _


class CodeModelMixin(models.Model):
    CODE_LENGTH = 8

    code = models.CharField(max_length=15, null=True, verbose_name=_("Codice"), editable=False, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(CodeModelMixin, self).save(force_insert, force_update, using, update_fields)
        if not self.code:
            self.code = self._get_code()
            super(CodeModelMixin, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True

    def _get_code(self):
        return format(self.pk, "0%sd" % self.CODE_LENGTH)

    def __unicode__(self):
        res = super(CodeModelMixin, self).__unicode__()
        if self.code:
            res += " (%s)" % self.code
        return res

