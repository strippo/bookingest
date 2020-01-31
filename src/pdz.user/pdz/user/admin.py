from django.conf.urls import url
from django.contrib import admin


from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


from pdz.user.models import User
from pdz.user.forms import EmailUserCreationForm, EmailUserChangeForm


class EmailUserAdmin(UserAdmin):
    app_label = _("auth")
    ordering = None
    add_form = EmailUserCreationForm
    form = EmailUserChangeForm
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_superuser', 'is_active', 'groups')
    readonly_fields = ('date_joined','last_login')
    filter_horizontal = ('groups', 'user_permissions',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name' )}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser',
                                       'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Profilo'), {'fields': ()}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    def get_urls(self):
         from django.conf.urls import patterns
         info = self.model._meta.app_label, self.model._meta.module_name

         return patterns('',
             url(r'^(\d+)/password/$',
              self.admin_site.admin_view(self.user_change_password), name="%s_%s_password" % info)
         ) + super(EmailUserAdmin, self).get_urls()


admin.site.register(User, EmailUserAdmin)
