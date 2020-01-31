# coding: utf-8
from django.contrib import admin
from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from pdz.admin.base import BaseModelAdmin
from django.utils.translation import ugettext as _
from pdz.users.models import User
from pdz.warehouse.models import Product, ProductMovement
from pdz.warehouse.filters import QuantityStatusFilter


class ProductAdmin(BaseModelAdmin):
    app_label = _("Magazzino")
    list_display = ('code', 'title', 'price', '_available_quantity', 
                    '_ingoing_link', '_outgoing_link'
                    )
    fields = ('code', ('title', 'price'),)
    search_fields = ('code', 'title', 'price')
    list_filter = (QuantityStatusFilter,)

    def _available_quantity(self, obj):
        style = "color: white; padding:5px 4px 5px 5px; font-weight: bold;"
        if obj.get_available_quantity() < 2:
            style += "background: red"
        else:
            style += "background: green"
        return '<span style="' + style + '">%s</span>' % obj.get_available_quantity()
    _available_quantity.short_description = "Quantità disponibile"
    _available_quantity.allow_tags = True
    
    def _ingoing_link(self, obj):
        url = reverse("admin:warehouse_productmovement_add")
        qs = '?in&product_pk=%s' % obj.pk
        return """<a href="%s%s">
        <i class="fa fa-level-up fa-2x"></i>
        </a>""" % (url, qs)
    
    _ingoing_link.short_description = _("Carica")
    _ingoing_link.allow_tags = True
    
    def _outgoing_link(self, obj):
        url = reverse("admin:warehouse_productmovement_add")
        qs = '?out&product_pk=%s' % obj.pk
        return """<a href="%s%s">
        <i class="fa fa-level-down fa-2x"></i>
        </a>""" % (url, qs)

    _outgoing_link.short_description = _("Scarica")
    _outgoing_link.allow_tags = True


admin.site.register(Product, ProductAdmin)



class ProductMovementCreationForm(forms.ModelForm):
    class Meta:
        model = ProductMovement
        fieldsets = ('product', 'operator', 'quantity', 'user', 'movement_type')

    def __init__(self, *args, **kwargs):
        if kwargs.has_key('initial'):
            if kwargs['initial'].has_key('product_pk'):
                kwargs['initial']['product'] = kwargs['initial']['product_pk']
            if kwargs['initial'].has_key('in'):
                kwargs['initial']['movement_type'] = 1
                self.base_fields['movement_type'].widget.attrs['class'] = 'hidden'
            elif kwargs['initial'].has_key('out'):
                kwargs['initial']['movement_type'] = 2
                self.base_fields['movement_type'].widget.attrs['class'] = 'hidden'
        super(ProductMovementCreationForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(active=True)

    def clean(self):
        cleaned_data = super(ProductMovementCreationForm, self).clean()
        user = cleaned_data.get('user')
        movement_type = cleaned_data.get('movement_type')
        if movement_type == 2 and not user:
            raise forms.ValidationError("Per i prodotti in uscita selezionare un Cliente!")
        if movement_type == 1 and  user:
            raise forms.ValidationError("Per i prodotti in entrata non selezionare Clienti!")
        return cleaned_data

class ProductMovementAdmin(BaseModelAdmin):
    app_label = _("Magazzino")
    list_display = ('movement_type', 'product', 'created', 'quantity',  'operator', '_get_user')
    list_filter = ('movement_type', 'product', "operator", )
    fields = (('product',), ('operator', 'quantity', 'user', 'movement_type'))
    form = ProductMovementCreationForm
    list_display_links = ('movement_type', 'product')
    
    def _get_user(self, obj):
        if obj.user:
            return obj.user
        return "--"

    _get_user.short_description = _("Cliente")
    _get_user.allow_tags = True

    def response_add(self, request, obj, post_url_continue=None):
        """This makes the response after adding go to another apps changelist for some model"""
        if obj.user:
            return HttpResponseRedirect(reverse("admin:users_user_view", args=[obj.user.pk]))
        return super(ProductMovementAdmin, self).response_add(request, obj, post_url_continue=None)

admin.site.register(ProductMovement, ProductMovementAdmin)