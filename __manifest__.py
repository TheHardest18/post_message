# -*- coding: utf-8 -*-
{
    'name': "post_message",

    'summary': """
        Add default message in log note
        """,

    'description': """
    this module fulfills the function of adding a 
    default log note in a sales order
    """,

    'author': "Isias Mateo: isias1626@gmail.com",
    'category': 'Uncategorized',
    'version': '13.0.0.0.1',
    'depends': ['base','sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
