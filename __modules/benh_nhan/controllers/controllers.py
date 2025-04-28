# -*- coding: utf-8 -*-
# from odoo import http


# class BenhNhan(http.Controller):
#     @http.route('/benh_nhan/benh_nhan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/benh_nhan/benh_nhan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('benh_nhan.listing', {
#             'root': '/benh_nhan/benh_nhan',
#             'objects': http.request.env['benh_nhan.benh_nhan'].search([]),
#         })

#     @http.route('/benh_nhan/benh_nhan/objects/<model("benh_nhan.benh_nhan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('benh_nhan.object', {
#             'object': obj
#         })

