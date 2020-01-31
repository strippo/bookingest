from itertools import chain
from pdz.admin.views.mixins import AdminObjectMixin
from pdz.events.views.ajax import CalendarEventsView


class OperatorEventsView(AdminObjectMixin, CalendarEventsView):
    opts = None

    def get_events(self, start, end):
        obj = self.get_object()
        availabilites = obj.availabilites.filter(start__gte=start, end__lte=end)
        appointments = obj.appointments.filter(start__gte=start, end__lte=end)
        items = chain(availabilites, appointments)
        items = [o.to_dict() for o in items]
        return items
