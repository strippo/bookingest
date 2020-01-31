from bootstrap_admin.templatetags.bootstrap_template_tags import silence_without_field, _process_field_attributes
from django.template.loader_tags import register


@register.filter("append_attr")
@silence_without_field
def append_attr(field, attr):
    def process(widget, attrs, attribute, value):
        if hasattr(widget, "widgets"):
            [process(widget, widget.attrs, attribute, value) for widget in widget.widgets]
        elif attrs.get(attribute):
            attrs[attribute] += ' ' + value
        elif widget.attrs.get(attribute):
            attrs[attribute] = widget.attrs[attribute] + ' ' + value
        else:
            attrs[attribute] = value
    return _process_field_attributes(field, attr, process)
