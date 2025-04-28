# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ketquaxn(models.Model):
    _name = 'thxn.ketquaxn'
    _description = 'Kết quả xét nghiệm'

    contact_id = fields.Many2one("res.partner", string="Bệnh nhân", required=True, default=lambda self: self.env['res.partner'].search([], limit=1))
    loaiXN = fields.Selection(
        selection=[('huyethoc', 'Huyết học'), 
                   ('visinh', 'Vi sinh')],
        string='Loại xét nghiệm', 
        required=True
    )
    tenXN = fields.Char(string='Tên xét nghiệm', required=True)
    thoigianthuchien = fields.Datetime(string='Thời gian thực hiện', required=True)

class kqxn_huyethoc(models.Model):
    _inherit = 'thxn.ketquaxn'
    _description = 'Kết quả xét nghiệm huyết học'

    hongcau = fields.Float(string='Số lượng hồng cầu (triệu tế bào/µL)')
    bachcau = fields.Float(string='Số lượng bạch cầu (tế bào/µL)')
    tieucau = fields.Float(string = 'Số lượng tiểu cầu (ngàn tế bào/µL)')
    hemoglobin = fields.Float(string = 'Lượng Hemoglobin (g/dL)')

class kqxn_visinh(models.Model):
    _inherit = 'thxn.ketquaxn'
    _description = 'Kết quả xét nghiệm vi sinh'

    tenVK = fields.Char(string='Vi khuẩn gây bệnh')
    khangsinhdo = fields.Text(string='Kháng sinh đồ')
    tylekhangthuoc = fields.Float(string='Tỷ lệ kháng thuốc (%)')