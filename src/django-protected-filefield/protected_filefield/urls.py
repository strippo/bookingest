import os
import re

import protected_filefield.settings
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^%s(?P<path>.*)$' % re.escape(protected_filefield.settings.PRIVATE_URL.lstrip('/')),
                           view="protected_filefield.views.private_serve", kwargs={
                               "document_root": os.path.join(protected_filefield.settings.PRIVATE_ROOT)
                           }),
                       )
