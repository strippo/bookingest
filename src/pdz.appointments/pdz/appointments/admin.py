from pdz.base.forms import SingleUserField
from pdz.events.admin import PopupReloadMixin
from pdz.events.forms import InitialDateMixin
from django.contrib import admin
from pdz.admin.base import EnhancedModelAdmin
from pdz.appointments.models import Appointment
from django import forms
from django.utils.translation import ugettext as _
from pdz.users.models import User


class AppointmentForm(InitialDateMixin, forms.ModelForm):
    # user = SingleUserField(label=_("Cliente"))

    class Meta:
        model = Appointment

    def __init__(self,*args,**kwargs):
        super (AppointmentForm, self).__init__(*args,**kwargs) # populates the post
        self.fields['user'].queryset = User.objects.filter(active=True)


class AppointmentAdmin(PopupReloadMixin, EnhancedModelAdmin):
    form = AppointmentForm
    app_label = _("Calendario")
    ordering = ('-start',)
    list_display = ('__unicode__', 'user', '_date', '_schedule', 'total_minutes', '_cost', 'operator', '_done')
    list_filter = ('operator', 'user', 'service')

    fields = (('user', 'operator', 'service', 'cost'), ('start', 'end'), 'canceled')

    search_fields = ['description', ]

    def _cost(self, obj):
        return "&euro; %s " % obj.cost
    _cost.short_description = "Pagato"
    _cost.allow_tags = True

    def _date(self, obj):
        return "%s" %  obj.start.strftime("%d/%m/%Y")
    _date.short_description = "Data"
    
    def _schedule(self, obj):
        time = "%s - %s" % (
            obj.start.strftime("%H:%M"), obj.end.strftime("%H:%M")
        )
        return time
    _schedule.short_description = "Orario"

    def _done(self, obj):
        if obj.canceled:
            icon = "icon-no"
        else:
            icon = "icon-yes"
        return """<img style="display:block" src="/static/admin/img/%s.gif" />""" % icon
    _done.short_description = "Eseguito"
    _done.allow_tags = True
    # def _users(self, obj):
    #     return u"%s" % ", ".join('%s %s' % (n, s) for n, s in obj.users.values_list("name", "surname"))
    # _users.short_description = "Utenti"

    def get_readonly_fields(self, request, obj=None):
        fields = super(AppointmentAdmin, self).get_readonly_fields(request, obj)
        return fields


    class Media:
        js = ("supportpaths/js/appointment_edit.js",)

admin.site.register(Appointment, AppointmentAdmin)
