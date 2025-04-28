# -*- coding: utf-8 -*-
# from odoo import http


# class PhongKham(http.Controller):
#     @http.route('/phong_kham/phong_kham', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/phong_kham/phong_kham/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('phong_kham.listing', {
#             'root': '/phong_kham/phong_kham',
#             'objects': http.request.env['phong_kham.phong_kham'].search([]),
#         })

#     @http.route('/phong_kham/phong_kham/objects/<model("phong_kham.phong_kham"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('phong_kham.object', {
#             'object': obj
#         })

