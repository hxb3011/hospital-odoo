# -*- coding: utf-8 -*-
{
    'name': "Điều phối bệnh nhân",

    'summary': "Thực hiện việc điều phối bệnh nhân",

    'description': """
Chức năng cho phép Bác sĩ có thể đưa ra các chỉ định(y lệnh) và Điều dưỡng có thể điều phối bệnh nhân dựa theo y lệnh.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        # 'data/tiendo_data.xml',
        'views/dieuphoi_view.xml',
        'views/actions.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}

