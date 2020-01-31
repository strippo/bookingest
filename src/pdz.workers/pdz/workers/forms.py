from pdz.base.fields import PAutoModelSelect2Field
from pdz.workers.models import Operator
from pdz.user.forms import EmailUserCreationForm, EmailUserChangeForm
from django.core.urlresolvers import reverse
from django_select2 import AutoModelSelect2Field


class OperatorCreationForm(EmailUserCreationForm):
    class Meta:
        model = Operator

class OperatorChangeForm(EmailUserChangeForm):
    def __init__(self, *args, **kwargs):
        super(OperatorChangeForm, self).__init__(*args, **kwargs)
        info = self.instance._meta.app_label,self.instance._meta.module_name
        url = reverse("admin:%s_%s_password" % info, args=(self.instance.pk,))
        txt = self.fields["password"].help_text.replace("<a href=\"password/\"",  "<a href=\"%s\"" % url)
        self.fields["password"].help_text = txt


    class Meta:
        model = Operator

class SingleOperatorField(PAutoModelSelect2Field):
    queryset = Operator.objects.all()
    search_fields = ['first_name__icontains', "last_name__icontains", "code__icontains"]

    def security_check(self, request, *args, **kwargs):
            return request.user.is_authenticated
