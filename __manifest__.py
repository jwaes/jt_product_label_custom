# -*- coding: utf-8 -*-
{
    'name': "jt_product_label_custom",

    'summary': 'Adds a custom 2x4 label format (99.1 x 67.7 mm)',
    'description': """
        This module introduces a custom label format of 2x4 labels (99.1 x 67.7 mm) for product labeling.
    """,

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'wizard/product_label_layout_views.xml',
        'report/product_label_paperformat.xml',
        'report/product_label_report_templates.xml',
    ],
    # 'assets': {
    #     'web.report_assets_common': [
    #         'product_label_custom/static/src/css/product_label_custom.css',
    #     ],
    # },
    'installable': True,
    'application': False,
}