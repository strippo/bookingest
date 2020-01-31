from functools import update_wrapper

from django.contrib import admin
from pdz.admin.views.view import View
from django.core.urlresolvers import reverse, resolve
from django.http import HttpResponseRedirect


class BaseModelAdmin(admin.ModelAdmin):
    app_label = None
    tools_items = []
    in_menu = True
    list_per_page = 30

    def changelist_view(self, request, extra_context=None):
        extra_context = {'admin_app_label': self.app_label or self.model._meta.app_label}
        return super(BaseModelAdmin, self).changelist_view(request, extra_context)

    def get_tools_items(self, object, **kwargs):
        return self.tools_items


class EnhancedModelAdmin(BaseModelAdmin):
    """Model admin with views"""
    view_cls = View
    tools_items = []

    def get_tools_items(self, request, obj, info):
        items = self.tools_items or []  # super(BaseModelAdmin, self).get_tools_items(request, obj, info)
        if super(admin.ModelAdmin, self).has_delete_permission(request, None) and self.in_view(request):
            items.insert(0,
                         ("<i class='fa fa-trash fa-2x'></i>",
                          reverse("admin:%s_%s_delete" % info, args=(obj.pk,)), "btn-danger"),
                         )
        if super(admin.ModelAdmin, self).has_change_permission(request, None) and self.in_view(request):
            items.insert(0,
                         ("<i class='fa fa-edit fa-2x'></i>",
                          reverse("admin:%s_%s_change" % info, args=(obj.pk,)), "btn-warning")
                         )

        return items

    def get_changelist(self, request, **kwargs):
        """
        Returns the ChangeList class for use on the changelist page.
        """
        from pdz.admin.views.view import ViewChangelist

        return ViewChangelist

    def get_extra_urls(self, info):
        urls = ()
        return urls

    def get_urls(self):
        urls = super(EnhancedModelAdmin, self).get_urls()
        from django.conf.urls import patterns, url

        def wrap(view):
            try:
                from django.views.generic import View

                if issubclass(view.im_self, View):
                    view = view(opts=self)
            except TypeError:
                pass

            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.module_name
        urlpatterns = patterns('')
        for regex, view, name in self.get_extra_urls(info):
            urlpatterns += patterns('', url(regex, wrap(view), name=name))

        urlpatterns += patterns('', url(r'^$', wrap(self.changelist_view), name='%s_%s_changelist' % info),
                                url(r'^add/$', wrap(self.add_view), name='%s_%s_add' % info),
                                url(r'^(\d+)/history/$', wrap(self.history_view), name='%s_%s_history' % info),
                                url(r'^(\d+)/delete/$', wrap(self.delete_view), name='%s_%s_delete' % info),
                                url(r'^(\d+)/change/$', wrap(self.change_view), name='%s_%s_change' % info),
                                url(r'^(?P<pk>\d+)/$', wrap(self.view_cls.as_view), name='%s_%s_view' % info), )

        urlpatterns_name = [x.name for x in urlpatterns]
        for url in urls:
            if url.name not in urlpatterns_name:
                urlpatterns.append(url)
        return urlpatterns

    def get_list_display(self, request):
        res = super(EnhancedModelAdmin, self).get_list_display(request)
        res += ('_get_change_link',)
        return res

    def response_post_save_add(self, request, obj):
        opts = self.model._meta
        post_url = reverse('admin:%s_%s_view' % (opts.app_label, opts.module_name), kwargs={'pk': obj.pk},
                           current_app=self.admin_site.name)

        return HttpResponseRedirect(post_url)

    response_post_save_change = response_post_save_add

    def _get_change_link(self, obj):
        info = self.model._meta.app_label, self.model._meta.module_name
        url = reverse("admin:%s_%s_change" % info, args=(obj.pk,))
        return """<a title="Modifica" href="%s"><span class="fa fa-edit fa-2x"></span></a>""" % url

    _get_change_link.allow_tags = True
    _get_change_link.short_description = ''

    def get_model_perms(self, request):
        perms = super(EnhancedModelAdmin, self).get_model_perms(request)
        perms["view"] = self.has_view_permission(request)
        return perms

    def get_view_permission(self):
        return 'view_%s' % self.opts.object_name.lower()

    def has_view_permission(self, request, obj=None):
        """
        Returns True if the given request has permission to view an object.
        Can be overridden by the user in subclasses.
        """
        opts = self.opts
        return request.user.has_perm(opts.app_label + '.' + self.get_view_permission())

    def has_change_permission(self, request, obj=None):
        """
           If obj is None we're in a changelist
        """
        # view or changelist
        if (obj is None and self.has_view_permission(request, obj)) or self.in_view(request):
            return True
        else:
            opts = self.opts
            return request.user.has_perm(opts.app_label + '.' + opts.get_change_permission())

    def in_view(self, request):
        url = resolve(request.path_info)
        return url.url_name.endswith("_view")
