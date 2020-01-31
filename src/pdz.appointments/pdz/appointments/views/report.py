from datetime import datetime, timedelta

from decimal import Decimal

from django.db.models import Sum
from django.views.generic.list import ListView
from pdz.appointments.models import Appointment
from pdz.enum.models import Service
from pdz.users.models import User
from pdz.workers.models import Operator


class AppointmentsListBase(ListView):
    model = Appointment
    report_by = None
    title = None

    def get_context_data(self, **kwargs):
        context = super(AppointmentsListBase, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['select_label'] = self.report_by._meta.verbose_name
        context['model_filters'] = self.report_by.objects.all()
        request = self.request
        if 'daterange' in request.GET.keys():
            if 'model_filters' in request.GET.keys() and request.GET['model_filters'] != "":
                context['model_filter'] = self.report_by.objects.get(pk=request.GET['model_filters'])
            start_str = context['daterange_from'] = request.GET['daterange'].split(' - ')[0]
            end_str = context['daterange_to'] = request.GET['daterange'].split(' - ')[1]
            start = datetime.strptime(start_str + ' 00:00:00', '%d/%m/%Y %H:%M:%S')
            end = datetime.strptime(end_str + ' 23:59:59', '%d/%m/%Y %H:%M:%S')
            context['header'] = self.get_header(start, end)
            dates = self.get_rows_dates(start, end)
            rows = []
            # retribution = 0
            services = Service.objects.all()
            for service in services:
                item = [service]
                for date in dates:
                    query = {'canceled': False, 'service': service, 'start__gte': date, 'end__lte': date+timedelta(days=1)}
                    res = self.object_list.filter(**query)
                    number = res.count()
                    if number:
                        minutes = res.aggregate(Sum('total_minutes'))
                        # retribution += number*service.cost
                        # earned = 0
                        # for result in res:
                        #     earned += result.cost
                        earned = res.aggregate(Sum('cost'))['cost__sum'] or 0
                        # item.extend((number, number*service.cost, minutes['total_minutes__sum'] or 0))
                        item.extend((number, earned, minutes['total_minutes__sum'] or 0))
                    else:
                        item.extend((0, '0.00', 0))
                rows.append(item)
            totale_row = ['Totale']
            total_report_retribution = 0
            for date in dates:
                services_number = 0
                date_retribution = 0
                total_minutes = 0
                for service in services:
                    query = {'canceled': False, 'service': service, 'start__gte': date, 'end__lte': date+timedelta(days=1)}
                    res = self.object_list.filter(**query)
                    number = res.count()
                    if number:
                        services_number += number
                        service_cost = 0
                        # for result in res:
                        #     service_cost += result.cost
                        # service_cost = service.cost*number
                        service_cost = res.aggregate(Sum('cost'))['cost__sum'] or 0.00
                        date_retribution += service_cost
                        minutes = res.aggregate(Sum('total_minutes'))
                        total_minutes += minutes['total_minutes__sum'] or 0
                totale_row.extend((services_number, date_retribution, total_minutes))
                total_report_retribution += Decimal(date_retribution)
            rows.append(totale_row)
            context['total_report_retribution'] = total_report_retribution
            context['rows'] = rows

        return context

    def get_queryset(self):
        queryset = super(AppointmentsListBase, self).get_queryset()
        request = self.request
        if 'daterange' in request.GET.keys():
            start = datetime.strptime(request.GET['daterange'].split(' - ')[0] + ' 00:00:00', '%d/%m/%Y %H:%M:%S')
            end = datetime.strptime(request.GET['daterange'].split(' - ')[1] + ' 23:59:59', '%d/%m/%Y %H:%M:%S')
            query = {'start__gte': start,
                     'end__lte':end}
            if 'model_filters' in request.GET.keys() and request.GET['model_filters'] != "":
                query[self.report_by._meta.module_name +'__pk'] = int(request.GET['model_filters'])
            queryset = queryset.filter(**query)
        else:
            queryset = queryset.none()
        return queryset

    def get_rows_dates(self, start, end):
        end += timedelta(days=1)
        header = self.get_days(start, end, 'datetimes')
        return header

    def get_header(self, start, end):
        end += timedelta(days=1)
        header = self.get_days(start, end, 'string')
        return header

    def get_days(self, start, end, mode):
        start_date = start.date()
        end_date = end.date()
        days_list = []
        for single_date in self.daterange(start_date, end_date):
            if mode == 'string':
                days_list.append(single_date.strftime("%d/%m %a").replace('Sun', 'Dom')
                                                                 .replace('Mon', 'Lun')
                                                                 .replace('Tue', 'Mar')
                                                                 .replace('Wed', 'Mer')
                                                                 .replace('Thr', 'Gio')
                                                                 .replace('Fri', 'Ven')
                                                                 .replace('Sat', 'Sab')
                                 )
            elif mode == 'datetimes':
                days_list.append(datetime(
                                year=single_date.year,
                                month=single_date.month,
                                day=single_date.day,
                            ))
        return days_list

    @staticmethod
    def daterange(start_date, end_date):
            for n in range(int ((end_date - start_date).days)):
                yield start_date + timedelta(n)


class OperatorAppointmentsList(AppointmentsListBase):
    report_by = Operator
    title = "Operatrici: Report Trattamenti"


class UserAppointmentsList(AppointmentsListBase):
    report_by = User
    title = "Clienti: Report Trattamenti"
