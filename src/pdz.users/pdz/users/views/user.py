#from pdz.users.forms.user import UserCreateForm
from django.core import mail
from django.core.mail.message import EmailMessage
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.core.urlresolvers import reverse

#
#class UserCreateView(CreateView):
#    model = User
#    form_class = UserCreateForm
#    template_name = "users/user_create.html"
#    opts = None
#
#
#    def get_context_data(self, **kwargs):
#        context = super(UserCreateView, self).get_context_data(**kwargs)
#        context["adminform"] = context["form"]
#        context["opts"] = self.model._meta
#        context["change"] = False
#        context["is_popup"] = False
#        context["save_as"] = False
#        context["has_delete_permission"] = False
#        context["has_add_permission"] = False
#        context["has_change_permission"] = False
#        context["title"] = "Compila scheda telefonica (mancano alcuni fields, valutare dove metterli!!)"
#        return context
#
#    def get_fieldsets(self, form):
#        return [(None, {'fields': [('name','surname', 'birth_date'),
#                                    'group_therapy',
#                                    ('possible_request', 'observation'),]})]
#
#
#    def get_form(self, form_class):
#        self.object = self.model()
#        form = super(UserCreateView, self).get_form(form_class)
#        opts = self.opts
#        adminForm = helpers.AdminForm(form, list(self.get_fieldsets(form)),
#                                      {},
#                                      model_admin=opts)
#        return adminForm
#
#    def post(self, request, *args, **kwargs):
#        """
#        Handles POST requests, instantiating a form instance with the passed
#        POST variables and then checked for validity.
#        """
#        form_class = self.get_form_class()
#        form = self.get_form(form_class)
#        if form.form.is_valid():
#            return self.form_valid(form)
#        else:
#            return self.form_invalid(form)
#
#
#    def form_valid(self, form):
#        # TODO implementare metodi di ricerca o creazione e redirect
#        pass

class SendMassMail(View):
    opts = None

    def send_email(self, request):
        emails = request.POST.getlist("emails")
        subject = request.POST.get("subject")
        text = request.POST.get("text")
        messages = []
        for email in emails:
            message = EmailMessage(subject, text, from_email=None, to=[email])
            messages.append(message)
            connection = mail.get_connection()   # Use default email connection
            connection.send_messages(messages)
            messages.add_message(request, messages.INFO, 'Email inviate con successo.')


    def post(self, request):
        self.send_email(request)
        return HttpResponseRedirect(reverse("admin:users_user_changelist"))
