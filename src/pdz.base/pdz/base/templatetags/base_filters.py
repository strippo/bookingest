import json

from django import template

register = template.Library()


@register.filter(name='select2_list')
def select2_list(value):
    items = [{"text": unicode(x), "id": x.pk} for x in value]
    return json.dumps(items)
