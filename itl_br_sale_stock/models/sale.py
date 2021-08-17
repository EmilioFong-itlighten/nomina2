# -*- coding: utf-8 -*-

from datetime import timedelta

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('order_line.price_total')
    def _amount_all(self):
        super(SaleOrder, self)._amount_all()
        for order in self:
            order.update({
                'amount_total': order.total_bruto - order.total_desconto +
                order.total_tax + order.total_seguro +
                order.total_despesas,
            })