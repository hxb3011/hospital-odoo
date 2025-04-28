from odoo import models, fields

class HoSoBenhAn(models.Model):
    _name = 'benhnhan.hosobenhan'
    _description = 'Hồ sơ bệnh án'

    benh_nhan_id = fields.Many2one('benhnhan.benhnhan', string='Bệnh nhân', required=True, ondelete='cascade')
    # ten_benh_nhan = fields.Char(
    #     string='Tên bệnh nhân',
    #     related='benh_nhan_id.partner_id.name',
    #     store=True,
    #     readonly=True)
    ngay_lap = fields.Date(string='Ngày lập', required=True)
    chan_doan = fields.Text(string='Chẩn đoán')
    ghi_chu = fields.Text(string='Ghi chú')
