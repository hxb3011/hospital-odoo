from odoo import models, fields

class PhanBoGiuong(models.Model):
    _name = 'phongkham.phanbogiuong'
    _description = 'Phân Bổ Giường'

    giuong_id = fields.Many2one('phongkham.giuong', string='Giường', required=True)
    # benh_nhan_id = fields.Char(string='Tên Bệnh Nhân', required=True)
    benh_nhan_id = fields.Many2one('benhnhan.benhnhan', string='Bệnh Nhân')
    # ten_benh_nhan = fields.Char(
    #     string='Tên bệnh nhân',
    #     related='benh_nhan_id.partner_id.name',
    #     store=True,
    #     readonly=True)
    ngay_nhap_vien = fields.Date(string='Ngày Nhập Viện', required=True)
    ngay_xuat_vien = fields.Date(string='Ngày Xuất Viện')
