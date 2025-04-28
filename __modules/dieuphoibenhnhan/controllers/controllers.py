# -*- coding: utf-8 -*-
# from odoo import http


# class Dieuphoibenhnhan(http.Controller):
#     @http.route('/dieuphoibenhnhan/dieuphoibenhnhan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dieuphoibenhnhan/dieuphoibenhnhan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dieuphoibenhnhan.listing', {
#             'root': '/dieuphoibenhnhan/dieuphoibenhnhan',
#             'objects': http.request.env['dieuphoibenhnhan.dieuphoibenhnhan'].search([]),
#         })

#     @http.route('/dieuphoibenhnhan/dieuphoibenhnhan/objects/<model("dieuphoibenhnhan.dieuphoibenhnhan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dieuphoibenhnhan.object', {
#             'object': obj
#         })

