# coding: utf-8
from pdz.users.call_reasons import CALL_REASONS
from pdz.users.models import User
from django import forms
from django.utils.translation import gettext as _


class UserForm(forms.ModelForm):
    class Meta:
        model = User


class UserAddForm(UserForm):
    # call_reason = forms.ChoiceField(label=_("Motivo chiamata"), choices=CALL_REASONS)
    # call_description = forms.CharField(label=_("Descrizione chiamata"), widget=forms.Textarea)
    # appointment_date = forms.DateTimeField(label=_("Data appuntamento"), required=False)
    # appointment_description = forms.CharField(label=_("Descrizione appuntamento"), required=False)

    class Meta:
        model = User
