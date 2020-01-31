import os
from django.conf import settings

buildout_dir = os.path.split(settings.MEDIA_ROOT)[0]

PRIVATE_URL = getattr(settings, "PRIVATE_URL", "/private/")
PRIVATE_ROOT = getattr(settings, "PRIVATE_ROOT", os.path.join(buildout_dir, "private"))
