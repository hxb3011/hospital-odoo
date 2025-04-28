# -*- coding: utf-8 -*-

from odoo import models, fields, api


class datlich(models.Model):
    _name = 'datlich.datlich'
    _description = 'Thông tin đặt lịch hẹn khám'

    contact_id = fields.Many2one("res.partner", string="Bệnh nhân", required=True, default=lambda self: self.env['res.partner'].search([], limit=1))
    thoigian = fields.Datetime(string="Thời gian hẹn khám", default=fields.Datetime.now)
    mota = fields.Text(string="Mô tả tình trạng bệnh nhân, nguyên do khám")
    trangthai = fields.Selection(
    [
        ('cho', 'Chờ khám'),
        ('dangkham', 'Đang khám'),
        ('dahuy', 'Đã huỷ'),
        ('daxong', 'Đã khám xong')
    ],
    string='Trạng thái',
    default='cho',
    required=True
)