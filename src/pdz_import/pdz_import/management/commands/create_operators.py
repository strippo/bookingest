# coding: utf-8
from pdz.enum.models import Service
from django.contrib.auth.models import Group
from pdz.workers.models import Operator
from django.core.management.base import BaseCommand
from django.db import transaction

OPERATORS = [
    {'code': '01', 'surname': 'D\'Andrea', 'name': 'Wanda'},
    {'code': '02', 'surname': 'Matei', 'name': 'Andreea'},
    {'code': '03', 'surname': 'Cavalieri', 'name': 'Giorgia'},
    {'code': '04', 'surname': 'Palmucci', 'name': 'Martina'}
]


class Command(BaseCommand):

    @transaction.commit_on_success
    def handle(self, *args, **options):
        for operator in OPERATORS:
            newoperator = Operator.objects.create(**operator)
            self.stdout.write("Creato Operatore %s" % newoperator)
        self.stdout.write("\n\nOPERATORI CREATI")