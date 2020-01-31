# coding: utf-8
from django.utils.translation import gettext as _
from django.db import models
from django.db.models import Sum
from pdz.base.models import BasicModel, BaseModel


class Product(BasicModel):
    code = models.CharField(max_length=25, verbose_name=_("Codice"), unique=True)
    price = models.DecimalField(verbose_name="Prezzo di vendita", max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _("Prodotto")
        verbose_name_plural = _("Prodotti")
        ordering = ('title',)

    def __unicode__(self):
        return "%s - %s" % (self.code, self.title)
    
    def get_incoming_quantity(self):
        incoming_movements = self.movements.filter(movement_type=1).aggregate(Sum('quantity'))
        # fa fatto l'aggregate del campo quantity
        return incoming_movements['quantity__sum']

    def get_outgoing_quantity(self):
        outgoing_movements = self.movements.filter(movement_type=2).aggregate(Sum('quantity'))
        # fa fatto l'aggregate del campo quantity
        return outgoing_movements['quantity__sum']

    def get_available_quantity(self):
        incoming = self.get_incoming_quantity() or 0
        outgoing = self.get_outgoing_quantity() or 0
        return incoming - outgoing


MOVEMENT_TYPES = (
    (1, _("Carico")),
    (2, _("Uscita"))
)
class ProductMovement(BaseModel):
    operator = models.ForeignKey("workers.Operator",
                             verbose_name=_("Operatrice"),
                             related_name="product_movements")
    user = models.ForeignKey("users.User", blank=True, null=True, verbose_name=_("Cliente"))
    product = models.ForeignKey(Product,
                             verbose_name=_("Prodotto"),
                             related_name="movements")
    movement_type = models.IntegerField(choices=MOVEMENT_TYPES, verbose_name=_("Carico/Uscita"),
                                        blank=False,
                                        null=True,
                                        default=1)
    quantity = models.PositiveIntegerField(default=1,
                                           verbose_name=_("Quantità"), )

    def __unicode__(self):
        return "%s" % self.product.title

    class Meta:
        verbose_name = _("Movimento Prodotto")
        verbose_name_plural = _("Movimenti Prodotti")
        ordering = ('-created',)