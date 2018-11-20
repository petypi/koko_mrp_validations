from odoo import models, api, _
from odoo.exceptions import ValidationError


class MRPProduction(models.Model):
    _inherit = "mrp.production"

    @api.one
    @api.constrains('product_qty', 'product_qty')
    def _check_fractional_production(self):
        qty_2b_produced = self.product_qty / self.product_uom_id.factor
        ratio = self.bom_id.product_qty / self.bom_id.product_uom_id.factor

        if not float(qty_2b_produced/ratio).is_integer():
            raise ValidationError(
                _("BoM %s, cannot produce %s Unit(s) of %s by consuming %s Unit(s). "
                  "Please ensure that you consume whole numbers." % (
                    self.bom_id.product_tmpl_id.name,
                    self.product_qty,
                    '[%s] %s' % (self.product_id.default_code, self.product_id.name),
                    qty_2b_produced / ratio
                ))
            )

MRPProduction()
