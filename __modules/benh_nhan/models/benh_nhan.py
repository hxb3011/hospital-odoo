from odoo import models, fields

class BenhNhan(models.Model):
    _name = 'benhnhan.benhnhan'
    _description = 'Bệnh nhân'

    partner_id = fields.Many2one('res.partner', string='Thông tin liên hệ', required=True, ondelete='cascade')
    name = fields.Char(
    string='Tên bệnh nhân',
    related='partner_id.name',
    store=True,
    readonly=False)
    cmnd_cccd = fields.Char(string='CMND/CCCD', unique=True)
    ho_so_ids = fields.One2many('benhnhan.hosobenhan', 'benh_nhan_id', string='Hồ sơ bệnh án')
    def name_get(self):
        result = []
        for record in self:
            name = record.partner_id.name or "Không tên"
            result.append((record.id, name))
        return result