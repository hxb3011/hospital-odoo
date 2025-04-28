# -*- coding: utf-8 -*-
# from odoo import http


# class Thxn(http.Controller):
#     @http.route('/thxn/thxn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/thxn/thxn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('thxn.listing', {
#             'root': '/thxn/thxn',
#             'objects': http.request.env['thxn.thxn'].search([]),
#         })

#     @http.route('/thxn/thxn/objects/<model("thxn.thxn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('thxn.object', {
#             'object': obj
#         })

