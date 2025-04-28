from odoo import models, fields

class GiuongBenhVien(models.Model):
    _name = 'phongkham.giuong'
    _description = 'Giường Bệnh Viện'

    name = fields.Char(string='Tên Giường', required=True)
    phong_id = fields.Many2one('phongkham.phongkham', string='Phòng', required=True)
    trang_thai = fields.Selection([
        ('trong', 'Trống'),
        ('co_benh_nhan', 'Có bệnh nhân'),
        ('dang_sua', 'Đang sửa'),
    ], string='Trạng thái', default='trong')
