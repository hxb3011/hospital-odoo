# -*- coding: utf-8 -*-
{
    'name': "Quản lý bệnh nhân",

    'description': "Module quản lý bệnh nhân",

    'author': "TH",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/benhnhan_views.xml',
        'views/hosobenhan_views.xml'
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "installable": True,
    "application": True,
}

