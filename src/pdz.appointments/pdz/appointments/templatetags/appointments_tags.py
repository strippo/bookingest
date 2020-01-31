import datetime
from django import template
register = template.Library()


@register.inclusion_tag('appointments/templatetags/expert_appointments.html', takes_context=True)
def show_expert_appointments(context):
    request = context['request']
    now = datetime.datetime.now()
    context['old_appointments'] = request.user.expert.appointments.filter(end__lte=now, start__gte=now - datetime.timedelta(days=7)).order_by('start')
    context['appointments'] = request.user.expert.appointments.filter(end__gte=now).order_by('start')
    return context