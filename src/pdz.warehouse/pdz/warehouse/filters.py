#coding: utf-8
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class QuantityStatusFilter(admin.SimpleListFilter):
    title = _('Stato Quantità')
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('1', _('Stock Normale')),
            ('2', _('In esaurimento')),
            ('3', _('Esaurito')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            ids = [x.pk for x in queryset if x.get_available_quantity() >= 5]
            return queryset.filter(pk__in=ids)
        if self.value() == '2':
            ids = [x.pk for x in queryset if (x.get_available_quantity() < 5 and x.get_available_quantity() > 0)]
            return queryset.filter(pk__in=ids)
        if self.value() == '3':
            ids = [x.pk for x in queryset if x.get_available_quantity() == 0]
            return queryset.filter(pk__in=ids)
        
