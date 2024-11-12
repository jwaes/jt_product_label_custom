from odoo import models, fields

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection(
        selection_add=[('99x67_2x4', '2 x 4 (99.1 x 67.7 mm)')],
        ondelete={'99x67_2x4': 'set default'},
    )

    def _get_label_layout(self):
        res = super()._get_label_layout()
        res.update({
            '99x67_2x4': {
                'paperformat': 'paperformat_label_99x67_2x4',
                'rows': 4,
                'cols': 2,
                'height': 67.7,
                'width': 99.1,
                'dpi': 90,
            },
        })
        return res
