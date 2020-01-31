#!/usr/bin/python


import sys
sys.path[0:0] = [
    '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/Django-1.5.1-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/djc.recipe2-2.1-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/django_tinymce-1.5.1-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/sorl_thumbnail-11.12-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/South-0.8.1-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/MySQL_python-1.2.5-py2.7-linux-x86_64.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/distribute-0.7.3-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/django_localflavor-1.1-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/django_smart_selects-1.0.9-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/Django_Select2-4.2.1-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/pdz.base',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/pdz.admin',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/pdz.workers',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/pdz.user',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/pdz.users',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/pdz_import',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/pdz.events',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/pdz.enum',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/pdz.warehouse',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/pdz.appointments',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/django_dbbackup-1.9.0-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/bootstrap_admin-0.3.0-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/django-admin-menu',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/xhtml2pdf-0.0.5-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/django_xhtml2pdf-0.0.3-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/src/django-protected-filefield',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/django_overextends-0.3.2-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/sphinx_me-0.3-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/setuptools-10.1-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/reportlab-2.7-py2.7-linux-x86_64.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/Pillow-2.9.0-py2.7-linux-x86_64.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/pyPdf-1.13-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/html5lib-0.999-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/dropbox-3.22-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/boto-2.38.0-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/zc.recipe.egg-2.0.1-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/zc.buildout-2.3.1-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/six-1.9.0-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/requests-2.7.0-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/eggs/urllib3-1.11-py2.7.egg',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/parts/django',
  '/home/marco/develop/rogerpro/PANDIZUCCHERO/sites',
    ]

import os
try:
    from django.core.wsgi import get_wsgi_application
    IS_14_PLUS = True
except ImportError:
    from django.core.handlers.wsgi import WSGIHandler
    IS_14_PLUS = False

os.environ['DJANGO_SETTINGS_MODULE'] = "django_part_site.settings"


def app_factory(global_config, **local_config):
    """This function wraps our simple WSGI app so it
    can be used with paste.deploy"""
    if IS_14_PLUS:
        return get_wsgi_application()
    else:
        return WSGIHandler()

application = app_factory(global_config={})
