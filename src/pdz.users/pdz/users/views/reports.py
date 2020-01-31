from pdz.admin.views.mixins import AdminObjectMixin
from pdz.users.models import User
from django.views.generic import DetailView
from pdz.base.utils import render_to_pdf_response
from django.utils.translation import gettext as _


class ReportCheckinCard(AdminObjectMixin, DetailView):
    model = User
    opts = None
    template_name = "users/user_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ReportCheckinCard, self).get_context_data(**kwargs)
        #practices = Practice.objects.filter(user=self.object).order_by('created')
        # calls = Call.objects.filter(user=self.object).order_by('created')
        # if calls:
        #     context['call'] = calls[0]
        #if practices:
         #   context['practice'] = practices[0]
        return context

    def render_to_response(self, context, **response_kwargs):
        return render_to_pdf_response(self.template_name, context, _("scheda-accettazione.pdf"))
