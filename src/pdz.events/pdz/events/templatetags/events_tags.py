from django import template

register = template.Library()


@register.inclusion_tag('/calendar/templatetags/calendar_view.html')
def show_calendar():

    return {}