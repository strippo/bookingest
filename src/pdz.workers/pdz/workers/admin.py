from pdz.appointments.models import Appointment
from pdz.events.admin import PopupReloadMixin
from pdz.events.forms import InitialDateMixin
from pdz.workers.forms import OperatorCreationForm, OperatorChangeForm
from pdz.workers.views import OperatorEventsView
from pdz.user.admin import EmailUserAdmin
from django.core.urlresolvers import reverse
from django import forms
from django.contrib import admin

from pdz.admin.base import EnhancedModelAdmin, BaseModelAdmin

from pdz.workers.models import Operator, OperatorAvailability
from django.utils.translation import gettext as _



class OperatorAvailabilityForm(InitialDateMixin, forms.ModelForm):
    class Meta:
        model = OperatorAvailability


class OperatorAvailabilityAdmin(PopupReloadMixin, BaseModelAdmin):
    in_menu = False
    form = OperatorAvailabilityForm
    fields = ( "start", "end")


admin.site.register(OperatorAvailability, OperatorAvailabilityAdmin)

class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 0
    max_num = 0
    verbose_name = _("Trattamento")
    verbose_name_plural = _("Trattamenti")
    fields = ("_title", "start", "end", "user", "_url",)
    readonly_fields = ("_title", "start", "end", "user", "_url",)

    def _url(self, obj):
        return """<a href="%s"><i class="glyphicon glyphicon-search"></i>&nbsp;Dettagli</a>""" % obj.appointment.get_absolute_url()

    _url.short_description = _(" ")
    _url.allow_tags = True

    def _title(self, obj):
        return obj.service.title

    _title.short_description = _("Trattamento")



class OperatorAdmin(EnhancedModelAdmin):
    app_label = _("Anagrafiche")
    ordering = ('code',)
    fields = (
        ('code', 'surname','name', 'color', 'active'),
    )
    inlines = (AppointmentInline, )

    search_fields = ("surname", "name")
    list_display = ("code", "surname", "name")
    # list_filter = (
    #     "city", "province",
    # )
    list_display_links = ('code', 'surname')
    # 
    # add_form = OperatorCreationForm
    # form = OperatorChangeForm

    def get_extra_urls(self, info):
        return []

    def get_extra_urls(self, info):
        urls = [
            (r"(?P<pk>\d+)/get_events/$", OperatorEventsView.as_view, "workers_operator_events"),
        ]
        return urls

    def get_tools_items(self, request, obj, info):
        tools_items = super(OperatorAdmin, self).get_tools_items(request, obj, info)
        tools_items = [
            (_("<i class='fa fa-file-text-o fa-2x' style='vertical-align: middle; margin-right:7px;'></i> TRATTAMENTI"),
            (reverse("operator_report") + "?model_filters=%s" % obj.pk), "btn-primary"),
            (_("<i class='fa fa-eur fa-2x' style='vertical-align: middle; margin-right:7px;'></i> VENDITE"),
            (reverse("operator_productmovement_report") + "?model_filters=%s" % obj.pk), "btn-primary"), 
        ] + tools_items
        return tools_items

admin.site.register(Operator, OperatorAdmin)
