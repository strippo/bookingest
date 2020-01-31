# coding: utf-8
from pdz.enum.models import Service
from django.core.management.base import BaseCommand
from django.db import transaction


SERVICES = [
    {'title': 'Trattamento corpo', 'cost':0},
    {'title': 'Trattamento viso', 'cost':0},
    {'title': 'Pulizia viso', 'cost':0},
    {'title': 'Baffi/sopracciglia', 'cost':0},
    {'title': 'Cera totale', 'cost':0},
    {'title': 'Cera parziale', 'cost':0},
    {'title': 'Massaggi', 'cost':0},
    {'title': 'Rituali', 'cost':0},
    {'title': 'Mani', 'cost':0},
    {'title': 'Semipermanente', 'cost':0},
    {'title': 'Piedi', 'cost':0},
    {'title': 'Ricostruzione', 'cost':0},
    {'title': 'Passata gel', 'cost':0},
    {'title': 'Refill', 'cost':0},
    {'title': 'Solarium', 'cost':0},
    {'title': 'Prodotti', 'cost':0},
    {'title': 'Trucco', 'cost':0},
    {'title': 'Altro', 'cost':0},
]

class Command(BaseCommand):

    @transaction.commit_on_success
    def handle(self, *args, **options):
        for service in SERVICES:
            newservice = Service.objects.create(**service)
            self.stdout.write("Creato Servizio %s" % newservice)
        self.stdout.write("\n\nSERVIZI CREATI")
