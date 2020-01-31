from datetime import datetime, timedelta

from django.db.models import Sum
from django.views.generic.list import ListView
from pdz.enum.models import Service
from pdz.users.models import User
from pdz.warehouse.models import ProductMovement, Product
from pdz.workers.models import Operator


class ProductMovementListBase(ListView):
    model = ProductMovement
    report_by = None
    title = None

    def get_context_data(self, **kwargs):
        context = super(ProductMovementListBase, self).get_context_data(**kwargs)
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
            products = Product.objects.all()

            for product in products:
                populated_row =  self.object_list.filter(product=product).count()
                if populated_row:
                    item = [product.title]
                    for date in dates:
                        query = {'product': product, 'created__gte': date, 'created__lte': date+timedelta(days=1), 'movement_type' : 2}
                        res = self.object_list.filter(**query)
                        number = res.count()
                        if number:
                            item.extend((number, number*product.price))
                        else:
                            item.extend((0, '0.00'))
                    rows.append(item)
            totale_row = ['Totale']
            total_report_retribution = 0
            for date in dates:
                products_number = 0
                date_retribution = 0
                for product in products:
                    if self.object_list.filter(created__gte=date, created__lte= date+timedelta(days=1)).count():
                        query = {'product': product, 'created__gte': date, 'created__lte': date+timedelta(days=1), 'movement_type' : 2}
                        res = self.object_list.filter(**query)
                        number = res.count()
                        if number:
                            products_number += number
                            billed = product.price*number
                            date_retribution += billed
                totale_row.extend((products_number, date_retribution))
                total_report_retribution += date_retribution
            rows.append(totale_row)
            context['total_report_retribution'] = total_report_retribution
            context['rows'] = rows

        return context

    def get_queryset(self):
        queryset = super(ProductMovementListBase, self).get_queryset()
        request = self.request
        if 'daterange' in request.GET.keys():
            start = datetime.strptime(request.GET['daterange'].split(' - ')[0] + ' 00:00:00', '%d/%m/%Y %H:%M:%S')
            end = datetime.strptime(request.GET['daterange'].split(' - ')[1] + ' 23:59:59', '%d/%m/%Y %H:%M:%S')
            query = {'created__gte': start,
                     'created__lte': end,
                     'movement_type': 2}
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


class OperatorProductMovementList(ProductMovementListBase):
    report_by = Operator
    title = "Operatrici: Report Vendite Prodotti "


class UserProductMovementList(ProductMovementListBase):
    report_by = User
    title = "Clienti: Report Prodotti Acquistati"
