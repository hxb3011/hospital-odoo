# -*- coding: utf-8 -*-
# from odoo import http


# class Datlich(http.Controller):
#     @http.route('/datlich/datlich', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/datlich/datlich/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('datlich.listing', {
#             'root': '/datlich/datlich',
#             'objects': http.request.env['datlich.datlich'].search([]),
#         })

#     @http.route('/datlich/datlich/objects/<model("datlich.datlich"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('datlich.object', {
#             'object': obj
#         })

