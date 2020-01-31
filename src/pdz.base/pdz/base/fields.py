from django_select2.fields import AutoModelSelect2Field

class PAutoModelSelect2Field(AutoModelSelect2Field):
    def prepare_value(self, value):
        val = super(PAutoModelSelect2Field, self).prepare_value(value)
        if val == "":
            val = None
        return val

