# -*- coding: utf-8 -*-

from odoo import models, fields, api


class thongtindieuphoi(models.Model):
    _name = "dieuphoi.thongtindp"
    _description = "Thông tin điều phối bệnh nhân"

    contact_id = fields.Many2one("res.partner", string="Bệnh nhân", required=True, default=lambda self: self.env['res.partner'].search([], limit=1))
    dichvu = fields.Selection(
        selection=[('xetnghiemhuyethoc', 'Xét nghiệm huyết học'), 
                   ('xetnghiemvisinh', 'Xét nghiệm vi sinh'),
                   ('xquang', 'Chụp X-Quang'),
                   ('sieuam', 'Siêu âm')],
        string='Dịch vụ chỉ định', 
        required=True
    )
    employee_id = fields.Many2one("hr.employee", string="Người chỉ định", default=lambda self: self.env['hr.employee'].search([], limit=1))
    tiendo = fields.Selection(
        selection=[('nhanylenh', 'Nhận y lệnh'), 
                   ('batdaudichvu', 'Bắt đầu thực hiện dịch vụ'),
                   ('hoanthanhdichvu', 'Hoàn thành dịch vụ')],
        string='Tiến độ thực hiện', 
        required=True,
        default='nhanylenh',
    )



