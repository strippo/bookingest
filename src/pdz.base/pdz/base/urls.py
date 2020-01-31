import os
from django.conf.urls import patterns, include, handler500, url
from django.conf import settings

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.db.models.loading import cache as model_cache
from pdz.appointments.views.report import OperatorAppointmentsList, UserAppointmentsList
from pdz.warehouse.views.report import UserProductMovementList, OperatorProductMovementList #ProductMovementList

if not model_cache.loaded:
    model_cache.get_models()
admin.autodiscover()

handler500 # Pyflakes

urlpatterns = patterns(
    '',
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r"^select2/", include("django_select2.urls")),
    url(r"^events/", include('pdz.events.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^workers/operator/report/', (OperatorAppointmentsList.as_view()), name="operator_report"),
    url(r'^users/user/report/', (UserAppointmentsList.as_view()), name="user_report"),
    url(r'^users/user/productmovement/report/', (UserProductMovementList.as_view()), name="user_productmovement_report"),
    url(r'^workers/operator/productmovement/report/', (OperatorProductMovementList.as_view()), name="operator_productmovement_report"),
    url(r'^', include(admin.site.urls)),
    url(r'^', include("protected_filefield.urls"))
)

urlpatterns += staticfiles_urlpatterns()
