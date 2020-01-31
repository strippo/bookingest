import datetime
from pdz.base.models import BasicModel
from django.core.urlresolvers import NoReverseMatch
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from pdz.events.colors import COLORS


class Event(BasicModel):
    now = datetime.datetime.now

    start = models.DateTimeField(default=now, verbose_name=_("Inizio"))
    end = models.DateTimeField(default=now, verbose_name=_("Fine"))
    color = models.CharField(max_length=7, verbose_name=_("Stanza"), choices=COLORS, null=True, blank=True)

    def to_dict(self, **kwargs):
        d = {
            'id': self.pk,
            'title': mark_safe(self.title),
            'description': mark_safe(self.description),
            'start': self.start.isoformat(),
            'end': self.end.isoformat(),
            'color': self.color,
        }
        try:
            d["url"] = self.get_absolute_url()
        except NoReverseMatch:
            pass
        d.update(kwargs)
        return d
