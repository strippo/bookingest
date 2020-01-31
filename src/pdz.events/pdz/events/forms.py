import datetime


class InitialDateMixin(object):
    DATE_FIELDS = ("start", "end")
    FORMAT = "%Y%m%d-%H%M%S"

    def __init__(self, *args, **kwargs):
        if "initial" in kwargs:
            initial = kwargs["initial"]
            for f in self.DATE_FIELDS:
                if f in initial:
                    initial[f] = datetime.datetime.strptime(initial[f], self.FORMAT)
        super(InitialDateMixin, self).__init__(*args, **kwargs)
