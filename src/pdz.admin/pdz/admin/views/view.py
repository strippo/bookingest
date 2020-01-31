# coding: utf-8
from itertools import chain
from pdz.admin.views.mixins import AdminObjectMixin
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.util import quote
from django.contrib.admin.views.main import ChangeList
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.views.generic import DetailView


class View(AdminObjectMixin, DetailView):
    """
     @type opts ModelAdmin
    """
    opts = ModelAdmin

    context_object_name = 'original'
    template_name = "view.html"

    class Meta:
        exclude = ("id", "created", "modified")

    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)

    def get_template_names(self):
        app_label = self.opts.model._meta.app_label
        object_name = self.opts.model._meta.object_name
        return ("admin/%s/%s/%s" % (app_label, object_name.lower(), self.template_name),
                "admin/%s/%s" % (app_label, self.template_name),
                "admin/%s" % self.template_name)

    def get_context_data(self, **kwargs):
        data = super(View, self).get_context_data(**kwargs)
        obj = data['object']
        opts = self.opts
        info = opts.model._meta.app_label, opts.model._meta.module_name

        data.update(self.get_change_view_data(obj))
        data['opts'] = self.opts.model._meta
        data['title'] = unicode(obj)
        data['tools_items'] = self.opts.get_tools_items(self.request, obj, info)
        return data

    def get_change_view(self):
        return self.opts.change_view(self.request, self.kwargs['pk']).context_data

    def get_change_view_data(self, obj):
        data = {}
        change_view = self.get_change_view()
        adminform = change_view['adminform']
        model = self.opts.model
        adminform.readonly_fields = [x.name for x in chain(model._meta.fields,
                                                           model._meta.many_to_many)]
        [setattr(f, "help_text", "") for f in model._meta.many_to_many]
        data['add'] = False
        data['adminform'] = adminform

        inline_admin_formsets = change_view['inline_admin_formsets']
        for formset in inline_admin_formsets:
            formset.readonly_fields = admin.util.flatten_fieldsets(formset.fieldsets)
            formset.formset.can_delete = False
            formset.formset.can_add = False
            formset.formset.extra = 0

        data['inline_admin_formsets'] = inline_admin_formsets
        return data

    def get_fields(self, model):
        return [x.name for x in model._meta.fields]

        # def get_object(self, queryset=None):
        #     return self.opts.get_object(self.request, self.kwargs['pk'])

    def dispatch(self, *args, **kwargs):
        obj = self.get_object()
        if not self.opts.has_view_permission(self.request, obj):
            return HttpResponseNotFound()
        return super(View, self).dispatch(*args, **kwargs)

class ViewChangelist(ChangeList):
    def url_for_result(self, result):
        pk = getattr(result, self.pk_attname)
        return reverse('admin:%s_%s_view' % (self.opts.app_label,
                                             self.opts.module_name),
                       args=(quote(pk),),
                       current_app=self.model_admin.admin_site.name)
