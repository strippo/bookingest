from django.contrib import admin
from django import template
from django.template.context import RequestContext
from django.utils.text import capfirst
from django.utils import six
from django.core.urlresolvers import reverse, NoReverseMatch


from django.template.loader import render_to_string

register = template.Library()


class MainMenuNode(template.Node):
    template_name = 'admin_menu/templatetags/admin_menu_sidebar.html'

    def render(self, context):
        """
        """
        request = context['request']
        action_list = [
            {'url': reverse("admin:warehouse_productmovement_add"), 'name': 'Aggiungi Movimento Prodotto'},
            {'url': reverse("admin:users_user_add"), 'name': 'Aggiungi Cliente'},
            {'url': reverse("admin:workers_operator_add"), 'name': 'Aggiungi Operatrice'},
        ]
        report_list = [
            {'url': reverse("operator_report"), 'name': 'OPERATRICI: Trattamenti'},
            {'url': reverse('operator_productmovement_report'), 'name': 'OPERATRICI: Vendite prodotti'},
            {'url': reverse('user_report'), 'name': 'CLIENTI: Trattamenti'},
            {'url': reverse('user_productmovement_report'), 'name': 'CLIENTI: Prodotti acquistati'},
            
        ]

        app_list = self.get_app_dict(context)
        context = RequestContext(request, {'app_list': app_list, 
                                           'action_list': action_list,
                                           'report_list': report_list})

        return render_to_string(self.template_name, context)

    def get_app_dict(self, context):
        request = context['request']
        app_dict = {}
        user = request.user
        for model, model_admin in admin.site._registry.items():
            if not getattr(model_admin, "in_menu", True):
                continue

            app_label = model._meta.app_label
            admin_app_label = getattr(model_admin, "app_label", None) or model._meta.app_label
            has_module_perms = user.has_module_perms(app_label)

            if has_module_perms:
                perms = model_admin.get_model_perms(request)

                # Check whether user has any perm for this module.
                # If so, add the module to the model_list.
                if True in perms.values():
                    info = (app_label, model._meta.module_name)
                    name = capfirst(model._meta.verbose_name_plural)

                    model_dict = {
                        'name': name,
                        'perms': perms,
                    }
                    if perms.get('change', False):
                        try:
                            model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=admin.site.name)
                        except NoReverseMatch:
                            pass
                    if perms.get('add', False):
                        try:
                            model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=admin.site.name)
                        except NoReverseMatch:
                            pass
                    if admin_app_label in app_dict:
                        app_dict[admin_app_label]['models'].append(model_dict)
                    else:
                        name = admin_app_label.title()
                        app_dict[admin_app_label] = {
                            'name': unicode(name),
                            'app_url': reverse('admin:app_list', kwargs={'app_label': app_label}, current_app=admin.site.name),
                            'has_module_perms': has_module_perms,
                            'models': [model_dict],
                        }

        # Sort the apps alphabetically.
        app_list = list(six.itervalues(app_dict))
        app_list.sort(key=lambda x: x['name'])

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

        return app_list

@register.tag
def show_main_menu(parser, token):
    return MainMenuNode()
