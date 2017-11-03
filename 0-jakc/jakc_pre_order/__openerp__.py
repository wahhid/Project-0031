# -*- coding: utf-8 -*-

{
    'name': 'Jakc Labs - Commerce Pre Order',
    'version': '9.0.0.1.0',
    'category': 'Workshop',
    'license': 'AGPL-3',
    'summary': 'Commerce Pre Order',
    'author': "Jakc Labs",
    'website': 'http://www.jakc-labs.com/',
    'depends': [
        'website',
        'sale',
    ],
    'data': [
        'views/templates.xml',
        'views/jakc_pre_order_menu.xml',
        'views/jakc_pre_order_view.xml',
    ],
    'installable': True,
    'application': True,
}
