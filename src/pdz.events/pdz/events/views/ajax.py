#coding: utf-8
import json
import datetime
from pdz.appointments.models import Appointment
from pdz.events.models import Event

from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


class CalendarEventsView(View):
    def get_tz_param(self, param):
        tz = self.request.GET[param]
        tz = float(tz)
        date = datetime.datetime.fromtimestamp(tz)
        return date

    def get_events(self):
        """
        @rtype : []
        """
        raise NotImplementedError()

    def get_start(self):
        return self.get_tz_param('start')

    def get_end(self):
        return self.get_tz_param('end')

    def get(self, request, *args, **kwargs):
        # events = [{'title': 'Evento test', 'start':'2013-08-08T13:15:30Z' }]
        start, end = self.get_start(), self.get_end()
        res = json.dumps(self.get_events(start, end))

        return HttpResponse(res, content_type='application/json')


class UpdateEvent(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateEvent, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        post = request.POST
        minuteDelta = datetime.timedelta(minutes=int(post["minuteDelta"]))
        dayDelta = datetime.timedelta(days=int(post["dayDelta"]))

        event = get_object_or_404(Event, pk=post["pk"])

        if not post["resize"] == "true":
            event.start += minuteDelta + dayDelta
        event.end += minuteDelta + dayDelta
        event.save()

        return HttpResponse("ok")


class GetCalendarEvents(CalendarEventsView):

    def get_events(self, start, end):
        # appointments = Appointment.objects.filter(canceled=False, start__gte=start, end__lte=end)
        # sul calendario vanno anche gli appuntamenti cancellati, che non escono nei report
        appointments = Appointment.objects.filter(start__gte=start, end__lte=end)
        # course_occurrences = CourseOccurrence.objects.filter(start__gte=start, end__lte=end)
        res = []
        for obj in appointments:
            res.append(obj.to_dict())
        #
        #for obj in course_occurrences:
        #    res.append(obj.to_dict())
        return res
