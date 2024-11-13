from odoo import models, fields

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection(
        selection_add=[('2x4xprice', '2 x 4 (99.1 x 67.7 mm) with price')],
        ondelete={'2x4xprice': 'set default'},
    )
