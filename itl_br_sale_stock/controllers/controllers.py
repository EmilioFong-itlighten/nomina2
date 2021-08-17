# -*- coding: utf-8 -*-
from odoo import http

# class ItlBrSaleStock(http.Controller):
#     @http.route('/itl_br_sale_stock/itl_br_sale_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/itl_br_sale_stock/itl_br_sale_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('itl_br_sale_stock.listing', {
#             'root': '/itl_br_sale_stock/itl_br_sale_stock',
#             'objects': http.request.env['itl_br_sale_stock.itl_br_sale_stock'].search([]),
#         })

#     @http.route('/itl_br_sale_stock/itl_br_sale_stock/objects/<model("itl_br_sale_stock.itl_br_sale_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('itl_br_sale_stock.object', {
#             'object': obj
#         })