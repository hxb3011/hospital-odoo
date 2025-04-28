from odoo import models, fields

class PhongKham(models.Model):
    _name = 'phongkham.phongkham'
    _description = 'Phòng Khám'

    name = fields.Char(string='Tên Phòng', required=True)
    loai_phong = fields.Selection([
        ('kham_benh', 'Khám bệnh'),
        ('noi_tru', 'Nội trú'),
    ], string='Loại Phòng', required=True)
    giuong_ids = fields.One2many('phongkham.giuong', 'phong_id', string='Danh sách giường')

    # trang_thai = fields.Selection([
    #     ('trong', 'Trống'),
    #     ('dang_su_dung', 'Đang sử dụng'),
    #     ('dang_sua', 'Đang sửa'),
    # ], string='Trạng thái', default='trong')
