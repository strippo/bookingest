from pdz.base.fields import PAutoModelSelect2Field
from pdz.users.models import User
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django_select2 import AutoModelSelect2MultipleField, AutoHeavySelect2MultipleWidget
from django_select2.fields import ModelSelect2Field, AutoModelSelect2Field
from django.utils.translation import ugettext as _

def add_plus_link(output, name, rel_to_model):
    link = []
    rel_to = rel_to_model
    info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
    related_url = reverse('admin:%s_%s_add' % info, current_app='admin')
    link.append(u'<a href="%s" class="add-another" id="add_id_%s" ' % (
        related_url, name))
    link.append(u'onclick="return showAddAnotherPopup(this);">')
    link.append(u'<img src="%s" width="10" height="10" alt="%s"/></a>'
                % (static('admin/img/icon_addlink.gif'), _('Add Another')))
    return output + mark_safe(u''.join(link))

class PlusAutoHeavySelect2MultipleWidget(AutoHeavySelect2MultipleWidget):
    def render(self, name, value, attrs=None, choices=()):
        out = super(PlusAutoHeavySelect2MultipleWidget, self).render(name, value, attrs, choices)
        return add_plus_link(out, name, self.choices.queryset.model)

class UserField(AutoModelSelect2MultipleField):
    queryset = User.objects.all()
    search_fields = ['name__icontains', "surname__icontains", "code__icontains"]
    widget = PlusAutoHeavySelect2MultipleWidget

    def security_check(self, request, *args, **kwargs):
        return request.user.is_authenticated

class SingleUserField(PAutoModelSelect2Field):
    queryset = User.objects.all()
    search_fields = ['name__icontains', "surname__icontains", "code__icontains"]

    def security_check(self, request, *args, **kwargs):
            return request.user.is_authenticated
