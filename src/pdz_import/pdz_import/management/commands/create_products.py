# coding: utf-8
import os
from django.core.management.base import BaseCommand
from django.db import transaction
import csv

from pdz.warehouse.models import Product

FILESDIR = os.path.split(__file__)[0] + '/csv/'

class Command(BaseCommand):

    @transaction.commit_on_success
    def handle(self, *args, **options):
        f = open(FILESDIR + 'prodotti_pdz.csv', 'r')
        rows = csv.DictReader(f, delimiter=';')
        for row in rows:
            self.parse_row(row)
            
            newproduct = Product.objects.create(title=row['title'], code=row['code'], price=0)
            self.stdout.write("Creato Prodotto %s" % newproduct)
        self.stdout.write("\n\nPRODOTTI CREATI")

    def parse_row(self, row):
        for f in row.keys():
            if f is None:
                del row[f]
            elif f == 'code':
                row[f].replace(" ", "")
            if isinstance(row[f], basestring):
                row[f].strip()

