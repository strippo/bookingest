from pdz.events.views.ajax import GetCalendarEvents, UpdateEvent
from django.conf.urls import patterns, url

urlpatterns = patterns("", url(r"get_events/$", GetCalendarEvents.as_view(), name="events.calendar_get_events"),
                       url(r"update_event/$", UpdateEvent.as_view(), name="events.calendar_update_event"), )
