from odoo import models, fields

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    label_type = fields.Selection(
        selection_add=[('2x4_99x67', '2 x 4 (99.1 x 67.7 mm)')],
        ondelete={'2x4_99x67': 'set default'}
    )
