from odoo import models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = ['|', ('name', operator, name), ('category_id.name', operator, name)]
        return self.search(domain + args, limit=limit).name_get()
