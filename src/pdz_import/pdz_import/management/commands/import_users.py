# -*- coding: utf-8 -*-
import os, datetime
from django.core.management.base import BaseCommand, CommandError
from pdz.users.models import User
from pdz.calls.models import Call
from pdz.practices.models import Practice
from pdz.enum.models import CaseType, MaritalStatus, Job, SchoolRanking
from django.db import transaction

import csv


DATE_FIELDS = ['birth_date', 'practice_created']
CALL_FIELDS = ['description']
PRACTICE_FIELDS = ['title', 'created']
EXCLUDED_FIELDS = ['mobile1', 'mobile2', 'phone1', 'phone2', 'observations']
# YEARS = ['2008','2009', '2010', '2011', '2012', '2013']
# YEARS = ['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007']
# YEARS = [
         # '1999', 
         # '2000',
         # '2001',
         # '2002',
         # '2003',
         # '2004',
         # '2005',
         # '2006',
         # '2007',
         # '2008',
         # '2009',
         # '2010',
         # '2011',
         # '2012',
         # '2013'
         # ]
YEARS = [
            '2014',
        ]
FILESDIR = os.path.split(__file__)[0] + '/csv/'


class Command(BaseCommand):
    @transaction.commit_on_success
    def handle(self, *args, **options):
        for year in YEARS:
            f = open(FILESDIR + 'utenti' + year + '.csv', 'r')
            rows = csv.DictReader(f, delimiter=';')
            for row in rows:            
                self.parse_row(row)
                user_obj = User()
                for field in row:
                    if field not in CALL_FIELDS and field not in PRACTICE_FIELDS and field not in EXCLUDED_FIELDS :
                        if field == "case_type":
                            obj_case, created = CaseType.objects.get_or_create(title=row[field])
                            setattr(user_obj, field, obj_case)
                        elif field == "marital_status":
                            obj_marital_status, created = MaritalStatus.objects.get_or_create(title=row[field])
                            setattr(user_obj, field, obj_marital_status)
                        elif field == "job":
                            obj_job, created = Job.objects.get_or_create(title=row[field])
                            setattr(user_obj, field, obj_job)
                        elif field == "school_ranking":
                            obj_school_ranking, created = SchoolRanking.objects.get_or_create(title=row[field])
                            setattr(user_obj, field, obj_school_ranking)
                        else:
                            setattr(user_obj, field, row[field])
                            
                # NUMERI DI TELEFONO
                if row.has_key('mobile2'):
                    mobile = row['mobile1'] + row['mobile2']
                elif row.has_key('mobile'):
                    mobile = row['mobile']
                else:
                    mobile = ''
                if row.has_key('phone2'):
                    phone = row['phone1'] + row['phone2']
                elif row.has_key('phone'):
                    phone = row['phone']
                else:
                    phone = ''
                setattr(user_obj, 'mobile', mobile)
                setattr(user_obj, 'phone', phone)
                
                #osservazioni
                if row.has_key('observations'):
                    setattr(user_obj, 'observations', row['observations'])

                user_obj.save()
                call_obj = Call(user=user_obj)
                practice_obj = Practice(user=user_obj)
                
                for field in row:
                    if field in CALL_FIELDS:
                        setattr(call_obj, field, row[field])
                    elif field in PRACTICE_FIELDS:
                        setattr(practice_obj, field, row[field])
                call_obj.save()
                practice_obj.save()
                self.stdout.write('\rUtente %s %s importato\n  creata call %s\n  creata practice %s\r' % (user_obj.name,
                                                                                                            user_obj.surname,
                                                                                                            call_obj.description,
                                                                                                            practice_obj.title))
            f.close()
        years = ' '.join(YEARS)
        self.stdout.write('\n\n\nIMPORTAZIONE ANNI %s COMPLETATA\n' % (years))
        
        
    def parse_row(self, row):
        for f in row.keys():
            if f is None:
                del row[f]
            elif f in DATE_FIELDS:
                try:
                    row[f] = datetime.datetime.strptime(row[f], '%d/%m/%Y')
                except ValueError:
                    row[f] = None
            elif f == 'code':
                row[f].replace(" ", "")
                # if User.objects.filter(code=row[f]):
                    # row[f] = '0' + row[f]
                while User.objects.filter(code=row[f]):
                    row[f] = '0' + row[f]
            if isinstance(row[f], basestring):
                row[f].strip()