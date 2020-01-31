import datetime
from django import template
from pdz.users.models import User
from pdz.warehouse.models import Product

register = template.Library()


@register.inclusion_tag('users/templatetags/users_homebox.html', takes_context=True)
def users_homebox(context):
    context['users_number'] = User.objects.all().count()
    return context
