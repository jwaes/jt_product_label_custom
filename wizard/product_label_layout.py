from odoo import models, fields, api

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    # Extend the print_format field
    print_format = fields.Selection(
        selection_add=[('2x4', '2 x 4 (99.1 x 67.7 mm)')],
        ondelete={'2x4': 'set default'},
    )

    def process(self):
        self.ensure_one()

        if self.print_format == '2x4':
            xml_id = 'product_label_custom.report_product_template_label_2x4'
            data = self._prepare_report_data_only()
        else:
            # Use the default process method for other formats
            return super(ProductLabelLayout, self).process()

        return self.env.ref(xml_id).report_action(None, data=data, config=False)

    def _prepare_report_data_only(self):

        active_model = ''
        if self.product_tmpl_ids:
            products = self.product_tmpl_ids.ids
            active_model = 'product.template'
        elif self.product_ids:
            products = self.product_ids.ids
            active_model = 'product.product'
        else:
            raise UserError(_("No product to print, if the product is archived please unarchive it before printing its label."))

        # Build data to pass to the report
        data = {
            'active_model': active_model,
            'quantity_by_product': {p: self.custom_quantity for p in products},
            'layout_wizard': self.id,
            'price_included': 'xprice' in self.print_format,
        }      
        return data  
