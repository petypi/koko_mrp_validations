from odoo import models, api, _
from odoo.exceptions import ValidationError


class MRPBom(models.Model):
    _inherit = "mrp.bom"

    @api.one
    @api.constrains('bom_line_ids', 'product_id', 'product_uom_id')
    def _check_bom_fraction(self):
        for l in self.bom_line_ids:
            if not l.product_qty.is_integer():
                raise ValidationError(
                    _("The Component Product %s, has a partial Quantity of %s, please use whole numbers." %
                      (l.product_id.name, l.product_qty))
                )

MRPBom()
