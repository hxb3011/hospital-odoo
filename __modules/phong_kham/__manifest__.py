# -*- coding: utf-8 -*-
{
    'name': "Quản lý phòng khám",

    # 'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': "Module quản lý phòng khám - Phòng và phân bổ giường",

    'author': "TH",
    # 'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','benh_nhan'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/phongkham_views.xml',
        'views/phan_bo_giuong_views.xml',
        
        
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "installable": True,
    "application": True,
}

