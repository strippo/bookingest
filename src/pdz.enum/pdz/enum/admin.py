from django.contrib import admin

from pdz.admin.base import BaseModelAdmin
from pdz.enum.models import Service
from django.utils.translation import ugettext as _


class BaseEnumAdmin(BaseModelAdmin):
    ordering = ('title', 'description')
    list_display = ('title', 'description')
    list_filter = ('title', 'description')
    search_fields = ('title', 'description')


class ServiceAdmin(BaseEnumAdmin):
    app_label = _("Termini")
    list_filter = ()
    list_display = ('title', '_cost')
    fields = (('title', 'cost'),)
    
    def _cost(self, obj):
        return "&euro; %s" % obj.cost
    _cost.short_description = "Costo"
    _cost.allow_tags = True
    
admin.site.register(Service, ServiceAdmin)

# 
# class CountryAdmin(BaseEnumAdmin):
#     app_label = _("Termini")
# 
# admin.site.register(Country, CountryAdmin)
# 
# 
# class SchoolRankingAdmin(BaseEnumAdmin):
#     app_label = _("Termini")
# 
# admin.site.register(SchoolRanking, SchoolRankingAdmin)
# 
# 
# class MaritalStatusAdmin(BaseEnumAdmin):
#     app_label = _("Termini")
# 
# admin.site.register(MaritalStatus, MaritalStatusAdmin)
# 
# 
# class JobAdmin(BaseEnumAdmin):
#     app_label = _("Termini")
# 
# admin.site.register(Job, JobAdmin)
# 
# 
# class CaseTypeAdmin(BaseEnumAdmin):
#     app_label = _("Termini")
# 
# admin.site.register(CaseType, CaseTypeAdmin)
# 
# 
# class UnionTypeAdmin(BaseEnumAdmin):
#     app_label = _("Termini")
# 
# admin.site.register(UnionType, UnionTypeAdmin)
# 
# class FirstActionAdmin(BaseEnumAdmin):
#     app_label = _("Termini")
# 
# admin.site.register(FirstAction, FirstActionAdmin)
